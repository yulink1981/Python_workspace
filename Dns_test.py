import dns.resolver

#domain = input('Please input an domainL')
domain = 'www.cebbank.com'
d = dns.resolver.query(domain,'MX')
print(dns.ipv4)
print(d.response)