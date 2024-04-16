"""
Adds the client_ip to OBJECTNAME

Shows how to use self.pldb.object_get to retrieve the id
of a NetObject.
"""

OBJECTNAME = "/NetObjects/Trigger/Add To NetObject"

class Trigger(FirewallTrigger):
    def trigger(self):
        obj = self.pldb.object_get(OBJECTNAME)
        if obj is None:
            print "Couldn't find object '%s'" % OBJECTNAME
            return
        self.pld.dyn_add(obj.id, self.client_ip)
