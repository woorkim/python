import dhcppacket
import packethandler
import sys
import time
from ReliableRuleset import SimpleNetobjectRuleset

TIMEOUT = 30
PLHOST = "127.0.0.1"
PLUSER = "packetlogicd"
PLPASS = "secret2"


class DHCPPacketHandler(packethandler.UDPPacketHandler):

    def __init__(self, iface):
        packethandler.PacketHandler.__init__(self, iface)

        while True:
            try:
                self.rs = SimpleNetobjectRuleset("/NetObjects/DHCP",
                                                 PLHOST, PLUSER, PLPASS,
                                                 "1.3.6.1.4.1.15397.2.10.1.1.1", "DHCP",
                                                 ["By MAC", "By option-82",
                                                  "By relay-agent"])
            except IOError:
                t, v, tb = sys.exc_info()
                print "Caught IOError, retrying in a minute (%s)" % v
                time.sleep(60)
                continue
            break

        self.rs.zone.value_definition_add(9, "Packets", self.rs.zone.TYPE_MOMENT)
        self.rs.zone["Packets"] = 0
        self.rs.zone.value_definition_add(10, "Unparsable packets", self.rs.zone.TYPE_MOMENT)
        self.rs.zone["Unparsable packets"] = 0
        self.rs.zone.value_definition_add(11, "Packets (DHCPREQUEST)", self.rs.zone.TYPE_MOMENT)
        self.rs.zone["Packets (DHCPREQUEST)"] = 0
        self.rs.zone.value_definition_add(12, "Packets (DHCPACK)", self.rs.zone.TYPE_MOMENT)
        self.rs.zone["Packets (DHCPACK)"] = 0
        self.rs.zone.value_definition_add(13, "Ignored packets", self.rs.zone.TYPE_MOMENT)
        self.rs.zone["Ignored packets"] = 0
        self.rs.zone.register()

        self.requests = {}

    def handle_udpdata(self, data, props):
        self.rs.zone["Packets"] += 1

        if props['udp-dst'] not in [67, 68]:
            self.rs.zone["Unparsable packets"] += 1
            return

        try:
            pkt = dhcppacket.DHCPPacket(data)
        except:
            import traceback
            print "Bad dhcp packet:"
            traceback.print_exc()
            self.rs.zone["Unparsable packets"] += 1
            return

        if pkt.type == 'DHCPREQUEST':
            self.rs.zone["Packets (DHCPREQUEST)"] += 1
            self.requests[(pkt.xid, pkt.hwaddr)] = (time.time(), pkt)
        elif pkt.type == 'DHCPACK':
            self.rs.zone["Packets (DHCPACK)"] += 1
            ip = dhcppacket.decodeip(pkt.yiaddr)

            if ip != '0.0.0.0':
                o = []

                o.append("By MAC/%s" % pkt.hwaddr)

                (t, req) = self.requests.get((pkt.xid, pkt.hwaddr), (None, None))
                if req:
                    if "option-82" in req.options:
                        o82 = req.options["option-82"]
                        if "remote-id" in o82:
                            remote_id = o82['remote-id']
                        else:
                            remote_id = "<missing>"

                        if "circuit-id" in o82:
                            circuit_id = o82["circuit-id"]
                        else:
                            circuit_id = "<missing>"

                        o.append("By option-82/%s/%s" % (remote_id, circuit_id))

                    del self.requests[(pkt.xid, pkt.hwaddr)]

                if dhcppacket.decodeip(pkt.giaddr) != "0.0.0.0":
                    o.append("By relay-agent/%s" % dhcppacket.decodeip(pkt.giaddr))

                self.rs.enqueue(ip, o)
            else:
                self.rs.zone["Ignored packets"] += 1

        # timeout old requests..
        now = time.time()
        removes = []
        for k, v in self.requests.iteritems():
            if v[0] + TIMEOUT < now:
                removes.append(k)
        for k in removes:
            del self.requests[k]

    def run(self):
        try:
            packethandler.PacketHandler.run(self)
        except KeyboardInterrupt:
            pass
        self.rs.stop()
        print "done?"

ph = DHCPPacketHandler(sys.argv[1])
ph.run()
