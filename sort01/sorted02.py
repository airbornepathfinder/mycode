#!/usr/bin/env python3

iplist = ['10.8.2.1', '1.1.1.1', '255.255.255.255', '10.1.2.1', '10.2.1.2', \
'10.2.3.2', '10.7.2.1', '192.168.23.1', '192.168.66.1', '10.42.2.1', \
'10.11.10.2', '10.25.32.2', '10.27.21.1', '192.168.55.1']


#mynewlist = (sorted(listofstrings, key=len))

print('Currently iplist looks like this:', iplist)

print('\The results of sorted(iplist) function:', sorted(iplist))

iplistkeyed = sorted(iplist, key=len)

print('\nResults of sorted(iplist, key=len): ' + str(iplistkeyed))

bakiplistkeyed = sorted(iplist, key=len, reverse=True)

print('\nResults of sorted(iplist, key=len, reverse=True): ' + str(bakiplistkeyed))

dnsrecord_types =  [ 'a', 'MX', 'AAAA', 'CNAME', 'naptr', 'ns', 'svr', 'SOA' ]

print('\ndnsrecord_types loos like this:', dnsrecord_types)

print('\nresults o fsorted(dnsrecord_types):', sorted(dnsrecord_types))

print('Results of sorted(dnsrecord_types, key=str.lower):', sorted(dnsrecord_types, key=str.upper))

