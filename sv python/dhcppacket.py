import struct

DHCPReqFmt = "!BBBBLHH4s4s4s4s16s64s128sL"
DHCPReqSiz = struct.calcsize(DHCPReqFmt)

"""
   FIELD      OCTETS       DESCRIPTION
   -----      ------       -----------

   op            1  Message op code / message type.
                    1 = BOOTREQUEST, 2 = BOOTREPLY
   htype         1  Hardware address type, see ARP section in "Assigned
                    Numbers" RFC; e.g., '1' = 10mb ethernet.
   hlen          1  Hardware address length (e.g.  '6' for 10mb
                    ethernet).
   hops          1  Client sets to zero, optionally used by relay agents
                    when booting via a relay agent.
   xid           4  Transaction ID, a random number chosen by the
                    client, used by the client and server to associate
                    messages and responses between a client and a
                    server.
   secs          2  Filled in by client, seconds elapsed since client
                    began address acquisition or renewal process.
   flags         2  Flags (see figure 2).
   ciaddr        4  Client IP address; only filled in if client is in
                    BOUND, RENEW or REBINDING state and can respond
                    to ARP requests.
   yiaddr        4  'your' (client) IP address.
   siaddr        4  IP address of next server to use in bootstrap;
                    returned in DHCPOFFER, DHCPACK by server.
   giaddr        4  Relay agent IP address, used in booting via a
                    relay agent.
   chaddr       16  Client hardware address.
   sname        64  Optional server host name, null terminated string.
   file        128  Boot file name, null terminated string; "generic"
                    name or null in DHCPDISCOVER, fully qualified
                    directory-path name in DHCPOFFER.
   options     var  Optional parameters field.  See the options
                    documents for a list of defined options.

"""

DHCPFields = {
    1: ("op", None, None),
    2: ("htype", None, None),
    3: ("hlen", None, None),
    4: ("hops", None, None),
    5: ("xid", None, None),
    6: ("secs", None, None),
    7: ("flags", None, None),
    8: ("ciaddr", None, None),
    9: ("yiaddr", None, None),
    10: ("siaddr", None, None),
    11: ("giaddr", None, None),
    12: ("chaddr", None, None),
    13: ("sname", None, None),
    14: ("filename", None, None),
    15: ("cookie", None, None)
}


def decodehwaddr(hwbin):
    return (("%02X" * len(hwbin)) % struct.unpack("B" * len(hwbin), hwbin))


def DefaultDecode(code, length, payload):
    return payload


def DecodeIpList(code, length, payload):
    l = []
    n = length / 4
    for i in range(0, n):
        ip = struct.unpack("BBBB", payload[i * 4:i * 4 + 4])
        l.append("%d.%d.%d.%d" % (ip[0], ip[1], ip[2], ip[3]))
    return l


def DecodeInt1(code, length, payload):
        try:
                i, = struct.unpack("!B", payload[:length])
        except:
                i = 0
        return i


def DecodeInt2(code, length, payload):
        try:
                i, = struct.unpack("!H", payload[:length])
        except:
                i = 0
        return i


def DecodeInt4(code, length, payload):
        try:
                i, = struct.unpack("!I", payload[:length])
        except:
                i = 0
        return i


dhcp_types = {
    1: 'DHCPDISCOVER',
    2: 'DHCPOFFER',
    3: 'DHCPREQUEST',
    4: 'DHCPDECLINE',
    5: 'DHCPACK',
    6: 'DHCPNAK',
    7: 'DHCPRELEASE',
    8: 'DHCPINFORM',
    9: 'DHCPFORCERENEW',
    10: 'DHCPLEASEQUERY',
    11: 'DHCPLEASEUNASSIGNED',
    12: 'DHCPLEASEUNKNOWN',
    13: 'DHCPLEASEACTIVE'
}


def DecodeType(code, length, payload):
    t = struct.unpack('B', payload)[0]
    return dhcp_types.get(t, "UNKNOWN(%d)" % t)


def DecodeOption82(code, length, payload):
    ops = {1: 'circuit-id', 2: 'remote-id'}
    i = 0
    ret = {}
    while i < length:
        (typ, leng) = struct.unpack('BB', payload[i:i + 2])

        name = ops.get(typ, "Unknown (%d)" % typ)
        if leng == 0:
            ret[name] = "<empty>"
        else:
            ret[name] = decodehwaddr(payload[i + 2:i + leng + 2])

        i = i + 2 + leng
    return ret


def DecodePList(code, length, payload):
    paramlist = []
    for i in range(0, length):
        paramcode = struct.unpack('B', payload[i:i + 1])[0]
        if paramcode in dhcpoption:
            paramlist.append(dhcpoption[paramcode][0])
    return paramlist

dhcpoption = {
    # DHCP Options and BOOTP vendor extensions (RFC2132)
    1: ('subnet-mask', DecodeIpList),
    2: ('time-offset', DecodeIpList,),
    3: ('router', DecodeIpList),
    4: ('time-server', DecodeIpList),
    5: ('name-server', DecodeIpList),
    6: ('domain-name-server', DecodeIpList),
    7: ('log-server', DecodeIpList),
    8: ('cookie-server', DecodeIpList),
    9: ('lpr-server', DecodeIpList),
    10: ('impress-server', DecodeIpList),
    11: ('resource-locator-server', DecodeIpList),
    12: ('host-name', None),             # ASCII string
    13: ('boot-file-size', DecodeInt2),  # int2
    14: ('merit-dump-file', None),       # ASCII string
    15: ('domain-name', None),           # ASCII string
    16: ('swap-server', DecodeIpList),
    17: ('root-path', None),
    18: ('extensions-path', None),
    # IP Layer Parameters per Host
    19: ('ip-forward-enable', None),         # boolean
    20: ('non-local-source-routing', None),  # bool
    21: ('policy-filter', DecodeIpList),     # Address-Mask pairs
    22: ('max-datagram-size', DecodeInt2),
    23: ('default-ip-ttl', DecodeInt1),
    24: ('mtu-timeout', DecodeInt4),
    25: ('path-mtu-plateau-table', None),    # Int2 list, to be implemented
    # IP Parameters per Interface
    26: ('interface-mtu', DecodeInt2),
    27: ('all-subnets-local', None),
    28: ('broadcast-address', DecodeIpList),
    29: ('perform-mask-discovery', None),
    30: ('mask-supplier', None),
    31: ('perform-router-discovery', None),
    32: ('router-solicitation-address', DecodeIpList),
    33: ('static-route', DecodeIpList),  # dest-gateway pairs
    # Link layer parameters per Interface
    34: ('trailer-encapsulation', None),
    35: ('arp-cache-timeout', DecodeInt4),
    36: ('ethernet-encapsulation', None),
    # TCP Parameters
    37: ('default-tcp-ttl', DecodeInt1),
    38: ('tcp-keepalive', DecodeInt4),
    39: ('tcp-keepalive-garbage', None),
    # DHCP Extensions
    50: ('requested-ip-address', DecodeIpList),
    51: ('ip-address-lease-time', DecodeInt4),
    52: ('option-overload', None),
    53: ('message-type', DecodeType),
    54: ('server-identifier', DecodeIpList),
    55: ('parameter-request-list', DecodePList),
    56: ('message', None),
    57: ('max-dhcp-message-size', DecodeInt2),
    58: ('renewal-time', DecodeInt4),
    59: ('rebinding-time', DecodeInt4),
    60: ('vendor-class', None),
    61: ('client-identifier', None),  # TOOODOOOOO fix this.
    66: ('tftp-server-name', None),
    67: ('bootfile-name', None),
    82: ('option-82', DecodeOption82)
}


def DecodeOptions(opt):
    """Convert a binary block of dhcp options into a decoded dictionary."""
    idx = 0
    opts = {}
    # iterate over the buffer
    while idx < len(opt):
        # Get the option code
        code = struct.unpack("B", opt[idx:idx + 1])[0]
        # Skip 'pad' and 'end' options
        if code in [0, 255]:
            idx = idx + 1
            continue
        # Get the option payload length
        lgt = struct.unpack("B", opt[idx + 1:idx + 2])[0]
        idx = idx + 2

        # check if the option is supported and decode contents
        if code in dhcpoption:
            name, decode = dhcpoption[code]
            if decode:
                val = decode(code, lgt, opt[idx:idx + lgt])
            else:
                val = DefaultDecode(code, lgt, opt[idx:idx + lgt])
            opts[name] = val

        idx = idx + lgt
    return opts


def decodeip(ip):
    return ".".join(map(str, struct.unpack("BBBB", ip)))


class DHCPPacket:
    def __init__(self, packet):
        """Create an empty packet object, or fill info from
        supplied binary packet data."""

        for f in DHCPFields.keys():
            setattr(self, DHCPFields[f][0], "")

        self._decode(packet)

    def _decode(self, packet):
        """Decode binary data packet into oneself, unless malformed."""
        if len(packet) < DHCPReqSiz:
            raise ValueError("Packet too short")

        dhcpdata = struct.unpack(DHCPReqFmt, packet[:DHCPReqSiz])

        for i in DHCPFields.keys():
            setattr(self, DHCPFields[i][0], dhcpdata[i - 1])

        self.options = DecodeOptions(packet[DHCPReqSiz:])

        if len(self.chaddr) < self.hlen:
            raise ValueError("Bad chaddr len")

        self.hwaddr = decodehwaddr(self.chaddr[:self.hlen])
        self.type = self.options.get("message-type", "NOT_PRESENT")
