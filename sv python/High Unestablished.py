"""
Adds the host to OBJECTNAME

"""
OBJECTNAME = "/NetObjects/HostTrigger/High Unestablished"

class Trigger(HostTrigger):
    def trigger(self):
        obj = self.pldb.object_get(OBJECTNAME)
        if obj is None:
            print "Couldn't find object '%s'" % OBJECTNAME
            return
        self.pld.dyn_add(obj.id, self.ip)

	print "Adding %s with %s High Unestablished %s" % (self.ip, self.connections, self.name) 

    def reset(self):
        obj = self.pldb.object_get(OBJECTNAME)
        if obj is None:
		print "Could not remove %s from High Unestablished %s" % (self.ip, self.name)
		return
        self.pld.dyn_remove(obj.id, self.ip)
	print "Removing  %s with %s High Unestablished %s" % (self.ip, self.connections, self.name) 
