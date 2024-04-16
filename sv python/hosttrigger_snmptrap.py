"""
Simple example on how to send an SNMP Trap
"""

from simpletrap import trapGenerator

class Trigger(HostTrigger):
    def trigger(self):
        # an explicit manager and community can be specified in the
        # call below to have it use something else than the
        # system-wide configured values.
        # i.e  manager="192.168.1.250", community="mytraps"
        err = trapGenerator.send(trapoid=('PACKETLOGIC-MIB', 'pl2TrapGenericMsg'),
                                 vars=[('PACKETLOGIC-MIB',
                                        'pl2TrapMessage',
                                        '%s matching hosttrigger' % self.ip)])

        if err is False:
            print 'No manager defined, did not send trap.'
        elif err is not None:
            print err
