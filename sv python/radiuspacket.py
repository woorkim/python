import socket
import struct

codes = {1: "AccessRequest",
         2: "AccessAccept",
         3: "AccessReject",
         4: "AccountingRequest",
         5: "AccountingResponse",
         11: "AccessChallenge",
         12: "StatusServer",
         13: "StatusClient"}


def string(x):
    return x


def ipaddr(x):
    return socket.inet_ntoa(x)


def integer(x):
    res = 0
    while x:
        res *= 256
        res += ord(x[0])
        x = x[1:]
    return res

attribs = {1: ("User-Name", string),
           4: ("NAS-IP-Address", ipaddr),
           5: ("NAS-Port", integer),
           6: ("Service-Type", integer),
           7: ("Framed-Protocol", integer),
           8: ("Framed-IP-Address", ipaddr),
           31: ("Calling-Station-Id", string),
           42: ("Input-Octets", integer),
           43: ("Output-Octets", integer),
           46: ("Session-Time", integer)}


class RadiusPacket(object):
    def __init__(self, data):
        (code, _id, l, authenticator) = struct.unpack("!BBH16s", data[:20])
        self.code = codes.get(code, "Unknown (%d)" % code)
        self.id = _id
        self.authenticator = authenticator
        self.options = {}
        data = data[20:]
        while len(data) > 0:
            k, l = struct.unpack("!BB", data[:2])
            if l < 2:
                raise ValueError("Broken packet")
            val = data[2:l]

            k, f = attribs.get(k, ("Unknown (%d)" % k, string))
            self.options[k] = f(val)

            data = data[l:]

    def has_key(self, k):
        return k in self.options

    def get(self, k, default=None):
        return self.options.get(k, default)

    def __contains__(self, k):
        return k in self.options

    def __getitem__(self, k):
        return self.options[k]
