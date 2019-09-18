#!/usr/bin/env python3

import pyexcel

varfilename = input('What is the name of the file? Do not include extension ')

myexcelval = { }

varfilename = varfilename + ".xls"

excelrecords = pyexcel.iget_records(file_name=varfilename)

for x in excelrecords:
    totalsocket = x['ip'] + ":" + str(x['port'])
    myexcelval.update ( { x['service'] : totalsocket } )

print(myexcelval)


