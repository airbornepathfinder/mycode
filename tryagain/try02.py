#!/usr/bin/python3

import sys

while True:
    try:
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)
    except:
        print("We did not anticipate that:", sys.exc_info()[0])
        raise


