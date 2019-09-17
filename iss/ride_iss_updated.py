#!/usr/bin/env python3

import urllib.request
import json

majortom = 'http://api.open-notify.org/astros.json'

def main():
    groundctrl = urllib.request.urlopen(majortom)
    helmet = groundctrl.read()
    helmetson = json.loads(helmet.decode('utf-8'))
    print("\n\nConverted Python data")
    print(helmetson)
    print("\n\nPeople in Space: ", helmetson['number'])
    people = helmetson['people']
    for i in people:
        print(i['name'], "on the", i['craft'])
main()
