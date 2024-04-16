"""
The really trivial trigger: just prints debug output to the log.
"""

class Trigger(FirewallTrigger):
    def trigger(self):
        print "Connection triggered '%s': %s:%d<->%s:%d" % (self.name,
                                                            self.server_ip,
                                                            self.server_port,
                                                            self.client_ip,
                                                            self.client_port)
        #self.protocol
        #self.flags
        #self.client_is_local
        #self.server_is_local
        #self.untracked
        #self.flowsync
        #self.established
