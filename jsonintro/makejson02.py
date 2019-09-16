#!/usr/bin/env python3

import json

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, \
            {"name": "Arthur Dent", "speceis": "Human"}]

    print(hitchhikers)

    jsonstring = json.dumps(hitchhikers)

    print(jsonstring)

main()
