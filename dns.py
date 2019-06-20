import dns.query
import dns.message
import dns.rdataclass
import dns.rdatatype


class DinghyDns:
    """The Dinghy Ping """
    def __init__(self, redis_host, domain_response_code=None, domain_response_time_ms=None, request_url=None):
        self.redis_host = redis_host
        self.domain_response_code = domain_response_code
        self.domain_response_time_ms = domain_response_time_ms
        self.request_url = request_url
    
    
    qname = dns.name.from_text('amazon.com')
    q = dns.message.make_query(qname, dns.rdatatype.NS)
    answers = dns.query.udp(q, '127.0.0.1')
    print(answers)
