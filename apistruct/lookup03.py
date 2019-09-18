#!/usr/bin/env python3

import requests
import argparse, socket
import json

from pprint import pprint as pp

def brand(brand):
    brand = input("What brand of device are you searching for? ")
    brand = "&brand=" + brand
    return brand

def main():
    mytoken = '499cfd2f206da4ba3fda8beeaec73caa74f6a2fea5e9f4fb'
    myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
    mybuiltapi = myapi + "?token=" + mytoken
    
    brand = input("What brand of device are you searching for? ")
    brand = "&brand=" + brand


    myjson = requests.get(mybuiltapi + brand).json()

    for x in myjson:
        pp(x.keys())

if __name__ == '__main__':
    main()

