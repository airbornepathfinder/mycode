#!/usr/bin/env python3

import requests

def main():
    mytoken = '499cfd2f206da4ba3fda8beeaec73caa74f6a2fea5e9f4fb'
    myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
    mybuiltapi = myapi + "?token=" + mytoken
    
    brand = input("What brand of device are you searching for? ")
    brand = "&brand=" + brand


    myjson = requests.get(mybuiltapi + brand).json()

    for x in myjson:
        print(x)

if __name__ == '__main__':
    main()

