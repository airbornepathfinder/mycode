#!/usr/bin/env python03

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']

print("Currently the value of vendor:", vendors)

print("\nThe results of sorted() function:", sorted(vendors))

print("\nBut the value of the list hasn\'t actually changed:", vendors)

sortedvendors = sorted(vendors)

print('Our sorted vendor list looks like this: ' + str(sortedvendors))

baksortvendors = sorted(vendors, reverse=True)

print('Our sorted vendor list looks like this: ', baksortvendors)

vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', 'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']

print('Our new venderdeux list look like this: ', vendorsdeux)

print('Our sorted vendor list looks like this: ', sorted(vendorsdeux))


