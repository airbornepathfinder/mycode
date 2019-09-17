#!/usr/bin/env python3

import urllib.request
import json
import webbrowser
from pprint import pprint as pp

NASAAPI = 'https://api.nasa.gov/planetary/apod?'

MYKEY = 'api_key=9gOQ1yw7QQgvijT73Gw9gV87bnNuo3lMCbi5c48Y'


def main():
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY)
    nasaread = nasaapiobj.read()
    convertedjson = json.loads(nasaread.decode('utf-8'))
    print(convertedjson)
    input('\nThis is converted JSON. Press Enter to continue.')

    pp(convertedjson)
    input('\nThis is pretty printed JSON. Press Enter to continue.')

    print(convertedjson['explanation'])
    input('\nPress Enter to view this photo of the day')
    webbrowser.open(convertedjson['hdurl'])

main()

