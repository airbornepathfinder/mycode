#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET
tree = ET.parse("moviesdat.xml")
root = tree.getroot()
for movie in root.iter("moviesdat.xml"):
    print(movie.attrib)
input("Press Enter to Continue")

b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(b2tf) 

b2tf.attrib["title"] = "Back to the Future"
print(b2tf.attrib)

tree.write("moviesdatUPDATED.xml")
root = tree.getroot()

for movie in root.iter("movie"):
    print(movie.attrib)

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)

input("Press Enter to Continue")

for form in root.findall("./genre/decade/movie/format"):
    match = re.search(",",form.text)
    if match:
        form.set("multiple", "Yes")
    else:
        form.set("multiple", "No")

tree.write("moviesdatUPDATED.xml")

tree = ET.parse("moviesdatUPDATED.xml")
root = tree.getroot()

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)
input("Press Enter to continue")

for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, "\n")
input("Press Enter to continue")

for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)

action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, "decade")
new_dec.attrib["years"] = "2000s"

print(ET.tostring(action, encoding="utf8").decode("utf8"))
input("Press Enter to Continue")

xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

print(ET.tostring(action, encoding="utf8").decode("utf8"))
input("Press Enter to Continue")

tree.write("moviesdatUPDATED.xml")
tree = ET.parse("moviesdatUPDATED.xml")
root = tree.getroot()

print(ET.tostring(action, encoding="utf8").decode("utf8"))
input("Press Enter to Continue")

