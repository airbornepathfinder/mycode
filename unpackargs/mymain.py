#!/usr/bin/env python3

from jrpg import find

EXCLUDE = ["/usr", "/home", "/var"]

def getuserinput():
    lookfor = input("What pattern as I looking for (Example: *.txt or *.cfg) ")
    lookwhere = input("What is the path in which I should search? ")
    return (lookfor, lookwhere)

def main():
    """runtime code"""
    while(True):
        print("Results: ", find(*getuserinput(),EXCLUDE))
        if (input("\nPress n to quit or any other key to search again ").lower() == "n"):
            break

main()
