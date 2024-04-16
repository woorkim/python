"""
Adds the client_ip and server_ip to OBJECTNAME if they are in
any of the netblocks specified in RANGES.

Shows that it is possible to do some python code.
"""


OBJECTNAME = "/NetObjects/Trigger/Add To NetObject local"
RANGES = ["192.168.9.0/24", "10.100.0.0/16"]

def iptoint(ip):
    return sum([int(x)<<(8*(3-y)) for x, y in zip(ip.split("."),range(4))])

def ipinrange(ip, ran):
    [net, mask] = ran.split("/")
    ip = iptoint(ip)
    net = iptoint(net)
    if ip >= net and ip < (net + (1<<(32-int(mask)))):
        return True
    return False
    

class Trigger(FirewallTrigger):
    def trigger(self):
        obj = self.pldb.object_get(OBJECTNAME)
        if obj is None:
            print "Couldn't find object '%s'" % OBJECTNAME
            return

        for r in RANGES:
            if ipinrange(self.client_ip, r):
                self.pld.dyn_add(obj.id, self.client_ip)
                break

        for r in RANGES:
            if ipinrange(self.server_ip, r):
                self.pld.dyn_add(obj.id, self.server_ip)
                break
