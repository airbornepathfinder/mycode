#!/usr/bin/env python3

import os
import paramiko

def main():
    t = paramiko.Transport("10.10.2.3", 22)

    t.connect(username="bender", password="alta3")

    sftp = paramiko.SFTPClient.from_transport(t)

    for x in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("/home/student/filestocopy/" + x):
           sftp.put("/home/student/filestocopy/" + x, "/tmp/" + x)


    sftp.close()

main()




