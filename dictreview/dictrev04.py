#!/usr/bin/env python3

def main():
    vendordict = {'cisco': True, 'juniper': False, 'arista': True, 'netgear': True}
    custlist = ['acme', 'globlex corporation', 'soylent green', 'initech', 'umbrella corporation']

    print(dir(dict))

    print(dir(list))

    #custlist.keys()
    vendordict.get('juniper')
    #custlist.get('umbrella corporation')
    #custlist.update('nax')
    #vendordict.update({'cisco':False})
    #vendordict.sort()
main()
