import difflib
import sys , fileinput
text1 = '''Presentation of the API
=======================

The IP class allows a comfortable parsing and handling for most
notations in use for IPv4 and IPv6 addresses and networks. It was
greatly inspired by RIPE's Perl module NET::IP's interface but
doesn't share the implementation. It doesn't share non-CIDR netmasks,
so funky stuff like a netmask of 0xffffff0f can't be done here.
'''
text2 = '''
Presentation of the BPI
=======================

The IP class allows a comfortable parsing and handlingab for most
notations in use for IPv4 and IPv6 addresses and networks. It was
greatly inspired by RIPE's Perl modulel NET::IP's interface but
doesn't share the implementation. It doesn't share non-CIDR netmasks,
so funky stuff like a netmask of 0xffffAAf can't be done here1.
'''

text1_line = text1.splitlines()
text2_line = text2.splitlines()

d = difflib.HtmlDiff()
with open('res.html','w') as f:
    for line in d.make_file(text1_line,text2_line):
        f.write(line)
f.close()




#t = 'my..name..is..boob'
#
#print(t.split('..'))
