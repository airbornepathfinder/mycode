#!/usr/bin/env python3

import os
import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root,file))
            ziph.write(os.path.join(root,file))

dir2zip = input("What directory are we archiving today? ")

if os.path.isdir(dir2zip):
    zippedfn = input("What should we call the finished archive? ")
    zipfileobj = zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED)
    zipdir(dir2zip, zipfileobj)
    zipfileobj.close()

else:
    print("Run the script again when you have a valid directory to zip.")

