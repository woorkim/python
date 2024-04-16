"""
The really trivial trigger: just prints debug output to the log.
"""
class Trigger(ConnProtTrigger):
    def trigger(self):
        print "%s are matching trigger '%s'" % (self.addresses, self.name)

    def reset(self):
        # Never called
        pass
