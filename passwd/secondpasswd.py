#!/usr/bin/env python3

import paramiko
import os
import getpass

t = paramiko.Transport("10.10.2.3", 22)

t.connect(username="bender", password=getpass.getpass())

sftp = paramiko.SFTPClient.from_transport(t)

sftp.put("firstpasswd.py", "firstpasswd.py")

sftp.close()


