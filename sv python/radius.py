
import packethandler
import radiuspacket
import time
import sys
from ReliableRuleset import SimpleNetobjectRuleset

TIMEOUT = 10


class RadiusPacketHandler(packethandler.UDPPacketHandler):

    def __init__(self, path):
        packethandler.PacketHandler.__init__(self, path)
        self.requests = {}

        subobjects = ["By Calling Station", "By NAS Port", "By User-Name"]
        while True:
            try:
                self.rs = SimpleNetobjectRuleset("/NetObjects/RADIUS",
                                                 "127.0.0.1", "packetlogicd", "secret2",
                                                 "1.3.6.1.4.1.15397.2.10.3", "Radius", subobjects)
            except IOError:
                t, v, tb = sys.exc_info()
                print "Caught IOError, retrying in a minute (%s)" % v
                time.sleep(60)
                continue
            break

    def handle_udpdata(self, data, props):
        try:
            pkt = radiuspacket.RadiusPacket(data)
        except:
            print "Bad radius packet"
            return

        if pkt.code in ("AccessRequest", "AccountingRequest"):
            self.requests[(props['ip-src'], pkt.id)] = (time.time(), pkt)
        elif pkt.code in ("AccessAccept", "AccountingResponse"):
            t, req = self.requests.get((props['ip-dst'], pkt.id), (None, None))

            ip = None
            if req and req.get("Framed-IP-Address", "255.255.255.254") != "255.255.255.254":
                ip = req["Framed-IP-Address"]
            if pkt.get("Framed-IP-Address", "255.255.255.254") != "255.255.255.254":
                ip = pkt["Framed-IP-Address"]

            if not (req is None or ip is None):
                objs = []
                if "Calling-Station-Id" in req:
                    n = "By Calling Station/%s" % req["Calling-Station-Id"]
                    objs.append(n)

                if "NAS-Port" in req:
                    n = "By NAS Port/%s - %d" % (req.get("NAS-IP-Address", "Unknown"), req["NAS-Port"])
                    objs.append(n)

                if "User-Name" in req:
                    n = "By User-Name/%s" % req["User-Name"].replace("/", "")
                    objs.append(n)

                if len(objs) > 0:
                    self.rs.enqueue(ip, objs)

            if req:
                del self.requests[(props['ip-dst'], pkt.id)]

        elif pkt.code == "AccessReject":
            if (props['ip-dst'], pkt.id) in self.requests:
                del self.requests[(props['ip-dst'], pkt.id)]

        # timeout old requests..
        now = time.time()
        removes = []
        for k, v in self.requests.iteritems():
            if v[0] + TIMEOUT < now:
                removes.append(k)
        for k in removes:
            del self.requests[k]

    def run(self):
        packethandler.PacketHandler.run(self)
        self.rs.stop()

ph = RadiusPacketHandler(sys.argv[1])
ph.run()
