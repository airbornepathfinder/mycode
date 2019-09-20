#!/usr/bin/env python3

import json
import time
import sqlite3
import urllib.request

def walmartlookup(walmarturl, mykey, upckey):
    try:
        walmarturlobj = urllib.request.urlopen(walmarturl + mykey + upckey)
        return json.loads(walmarturlobj.read().decode('utf-8'))

    except:
        return False

def trackmeplease(tracktime, trackprice):
    conn = sqlite3.connect('price.db')
    try:
        conn.execute('''CREATE TABLE PRICE
        (TIME VARCHAR2 PRIMARY KEY NOT NULL,
        PRICE REAL NOT NULL);''')

    except:
        pass
    conn.execute("INSERT INTO PRICE (TIME,PRICE) VALUES (?,?)",(tracktime, trackprice))
    conn.commit()
    cursor = conn.execute("SELECT time, price from PRICE")
    for row in cursor:
        print("TIME = ", row[0])
        print("PRICE = ", row[1])
    print("Database operation done")
    conn.close()

def main():
    wurl = 'http://api.walmartlabs.com/v1/items?'
    wkey = 'apiKey=d7hjdvye4sky5cdwmmmtf3bf'

    wupc = '190198511270'
    wupc = "&upc=" + wupc

    print("Walmart Query URL is:", wurl, wkey, wupc)

    decodewalmart = walmartlookup(wurl, wkey, wupc)

    if decodewalmart:
        print("\Walmart Price on", time.ctime(), ": $" + str(decodewalmart['items'][0]['salePrice']))
        print("\nShould we track this data within the database?")

        if input("y/n: ").lower() == 'y':
            print(time.ctime())
            trackmeplease(time.ctime(), decodewalmart['items'][0]['salePrice'])
        else:
            print("\nThanks for checking prices!")
    else:
        print("The UPC lookup failed.")

main()



