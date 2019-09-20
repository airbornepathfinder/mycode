#!/usr/bin/env python3

import smtplib 
import getpass

def main():
    mypass = getpass.getpass("Enter your password:")
    myaddress = input("Enter your mail.com address:")

    content = """From:airbornepathfinder@mail.com\nSubject:Great Class More Work For Us\nHi, My name is"""
    mail = smtplib.SMTP('smtp.mail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myaddress, mypass)
    mail.sendmail('strikeyoface@mail.com', content)
    mail.close()

main()

