#!/usr/bin/env python3

def main():
    vendordict = {'cisco': True, 'juniper': False, 'arista': True, 'netgear': True}
    custlist = ['acme', 'globlex corporation', 'soylent green', 'initech', 'umbrella corporation']

    print(vendordict)

    print(dir(dict))

    vendordict.keys()
    vendordict.values()
    vendordict.get('juniper')

    vendordict.pop('netgear')

    vendordict.get('netgear')

    print(dir(list))

    custlist.append('cyberdyne')

    print(custlist)

main()
