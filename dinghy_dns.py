import dns.query
import dns.message
import dns.rdataclass
import dns.rdatatype


class DinghyDns:
    """The Dinghy Ping Dns info interface. Will query the localhost at 127.0.0.1"""
    def __init__(self, domain=None, rdata_type=dns.rdatatype.A):
        self.domain = domain
        self.rdata_type = rdata_type

    def dns_query(self):
        qname = dns.name.from_text(self.domain)
        q = dns.message.make_query(qname, self.rdata_type)
        response = dns.query.udp(q, '192.168.40.1')
        
        return response
