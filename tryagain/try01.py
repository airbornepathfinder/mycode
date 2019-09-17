#!/usr/bin/python3

while True:
    try:
        print('Enter a file name: ')
        name = input()
        myfile = open(name, 'w')
    except:
        print('Error with that file name! Try again...')
    finally:
        myfile.close()
        break
