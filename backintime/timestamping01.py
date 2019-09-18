#!/usr/bin/env python3

import time 
from datetime import datetime

def main():
    startTime = datetime.now()

    print('The startTime hour is:', startTime.hour)
    print('The startTime minute is:', startTime.minute)
    print('The startTime day is:', startTime.day)
    print('The startTime year is:', startTime.year)


    time.sleep(2)


    print('The code took:', datetime.now() - startTime, 'to run.')


if __name__ == '__main__':
    main()
