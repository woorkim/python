"""
The really trivial trigger: just prints debug output to the log.
"""
class Trigger(HostTrigger):
    def trigger(self):
        print "%s is matching trigger '%s'" % (self.triggering_object, self.name)

        """
        print "trigtype %d" % self.trigtype
        if self.trigtype in [self.TRIGTYPE_HOST_IN_NETOBJECT, self.TRIGTYPE_NETOBJECT, self.TRIGTYPE_NETOBJECT_CHILD]:
            print "netobjectid %d" % self.netobjectid #self.netobjectid is not valid for self.trigtype == self.TRIGTYPE_HOST

        print "is_host()=%d is_netobject()=%d" % (self.is_host(), self.is_netobject())
        if self.is_host():
            print "ip %s" % self.ip #Same as self.triggering_object
        if self.is_netobject():
            print "netobjectpath %s" % self.netobjectpath #Same as self.triggering_object

        print "bytes %d %d" % self.bytes
        print "speed %d %d" % self.speed
        print "conns %d %d" % self.connections
        print "uconnrate %d" % self.uconnrate
        print "cps %d %d" % self.cps
        print "ttls %d" % self.ttls
        print "internal_quality %d %d" % self.internal_quality
        print "external_quality %d %d" % self.external_quality
        """

    def reset(self):
        print "%s not matching '%s' anymore" % (self.triggering_object, self.name)

