import requests
from simpletrap import trapGenerator

url = 'http://127.0.0.1:42052/api/1/classifier-table'
tableid=12
value='FlowFlood' # Connection classifier Value

def send_trap(data):
    err = trapGenerator.send(trapoid=('PACKETLOGIC-MIB', 'pl2TrapGenericMsg'),
                             vars=[('PACKETLOGIC-MIB',
                                    'pl2TrapMessage',
                                    '%s' % data)])

    if err is False:
        print 'No manager defined, did not send trap.'
    elif err is not None:
        print err

class Trigger(HostTrigger):
    def trigger(self):
        key_str = self.distributed_field_list.replace("-","")
        print "Distribution field list (trigger): %s " % (self.distributed_field_list)
        res = requests.post(url, json={"cmd" : "add", "data": {"table": tableid, "key": key_str, "value": value}})
        json_obj = res.json()
        if (json_obj['status'] != "ok"):
            print "Error in HTTP post request (ADD) : %s" % (json_obj['result'])
        else:
            print "Success for HTTP post request (ADD)"
            send_trap("Flow flood threat detected on %s" % (self.distributed_field_list))

    def reset(self):
        key_str = self.distributed_field_list.replace("-","")
        print "Distribution field list (reset): %s " % (self.distributed_field_list)
        res = requests.post(url, json={"cmd" : "remove", "data": {"table": tableid, "key": key_str}})
        json_obj = res.json()
        if (json_obj['status'] != "ok"):
            print "Error in HTTP post request (Remove) : %s" % (json_obj['result'])
        else:
            print "Success for HTTP post request (Remove)"
            send_trap("Flow flood clear on %s" % (self.distributed_field_list))
