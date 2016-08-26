from IPy import IP

print(IP('10.1.112.0/24').version())
print(IP('::5').version())

ip = IP('10.1.9.0/24')
print(ip.len())
for x in ip:
    print(x)
print((IP('10.1.112.187')).get_mac())


print(IP('10.1.112.0-10.1.112.255',make_net=True))



