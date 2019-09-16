#!/usr/bin/env python3

def main():
    ## creat an empty list
    anotheremptylist = []

    ## add to our list with a list method
    ## The extend method expects exactly one argument
    anotheremptylist.extend('10.0.0.1', 'retro_game_server')

    ## display our list
    print(anotheremptylist)

main()
