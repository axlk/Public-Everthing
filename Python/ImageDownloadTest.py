#coding=utf-8

import urllib
import re
import os
import subprocess


checkURL = "http://www.jandan.net/ooxx"

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

"""
def getImg(html):
    reg = r".*(jpg|gif|png)$"
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    
    x = 0
    for imgurl in imglist:
        print imgurl
"""

#html = getHtml(checkURL)

#html = "what the fock, aa.png bb.png "
html = getHtml(checkURL)
#pattern = ".*(png|gif|jpg)#"
pattern = r'src="//(.*.jpg)"'
#pattern = r"^/.*jpg"
reobj = re.compile(pattern)
objlist = re.findall(pattern, html)

i = 0
for img in objlist:
    print img
    i = i+1
    #urllib.urlretrieve(img, "/home/zkun1983/Downloads/%s.jpg" %i)

    #cmd = "wget -P /home/zkun1983/Downloads/%s.jpg" %i + imgRealPath

    imgRealPath = "http://"+img
    print imgRealPath
    cmd = "wget -P /home/zkun1983/Downloads/"  +" "+ imgRealPath
    print cmd
    os.system(cmd)
    #urllib.urlretrieve(imgRealPath, "/home/zkun1983/Downloads/%s.jpg" %i)

print "count:",i

#print getImg(html)



