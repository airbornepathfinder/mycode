#!/usr/bin/env python3

import csv

with open('inventory.csv', mode='w') as csv_file:
    fieldnames = ['hostname', 'ip', 'service']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'hostname': 'dumbledore', 'ip': '192.168.9.22', 'service': 'objectstorage'})
    writer.writerow({'hostname': 'hermione', 'ip': '10.0.2.66', 'service': 'httpd'})
