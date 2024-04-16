"""
Adds client ip to OBJECTNAME if client ip is at lest MAX_COUNT of
the last ARRAY_SIZE times this trigger has triggered.

Shows how to use __init__ to setup datastructures that are kept
between trigger.
"""

ARRAY_SIZE = 10
MAX_COUNT = 5
OBJECTNAME = "/NetObjects/Trigger/If Same Client"

class Trigger(FirewallTrigger):
    def __init__(self):
        FirewallTrigger.__init__(self) # don't forget this!
        self.clients = ["0.0.0.0" for x in range(ARRAY_SIZE)]
        self.pos = 0

    def trigger(self):
        if self.clients.count(self.client_ip) > MAX_COUNT:
            print "%s accounted for more than %d of the last %d matches" % \
                  (self.client_ip, ARRAY_SIZE, MAX_COUNT)
            obj = self.pldb.object_get(OBJECTNAME)
            if obj is None:
                print "Couldn't find object '%s'" % OBJECTNAME
            else:
                self.pld.dyn_add(obj.id, self.client_ip)

        self.clients[self.pos] = self.client_ip
        self.pos += 1
        self.pos %= ARRAY_SIZE
