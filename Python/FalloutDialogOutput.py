import urllib
import re
import sys


urlHead = "http://fallout.wikia.com"
mainURL = urlHead+"/wiki/Category:Fallout:_New_Vegas_dialogue_files?page=1"
outputPath = "/Users/AxlK/Downloads/Fallout NV Texts/"


def FindTxtURL(url):
    urlObj = urllib.urlopen(url)
    html = urlObj.read()

    reg = r"href=\"/(.*.txt)\" "
    return re.findall(reg, html)


allTxtUrl = FindTxtURL(mainURL)

count = 0
txtURL = []
for url in allTxtUrl:
    legalURL = urlHead+"/"+url
    print legalURL+" %s" %count
    txtURL.append( legalURL )
    count = count+1

print "total txt : %s" %count
totalCount = count

#multi find 
def MultiRegFind(reg, text):
    return re.findall(reg, text, flags=re.DOTALL+re.MULTILINE)


def ExtractDialogContent(html):
    reg = "np-table-dialogue\">(.*?</table>)"
    tableContentWithNoHead = MultiRegFind(reg, html)
    
    #fix table head
    #print len(tableContentWithNoHead)
    count = 0 
    tableHead = "<div><p>"
    tableMedium ="</p><table border=\"1\">\n"
    tableTail = "</div>\n"

    retData = []
    for content in tableContentWithNoHead:
        count = count + 1
        content = tableHead + "Part_%s" %count + tableMedium + content + tableTail 
        retData.append(content)


    #tableContent = "<table border=\"1\">\n" + tableContentWithNoHead[0]
    return retData


#outputPath = "/home/zkun1983/FalloutTexts/"

count = 0
#export all 
for url in txtURL:


    #extract name 
    name = re.findall(r"wiki/(.*?).txt", url)[0]
    count = count + 1
    print "process url :" + name + " count : %s/%s" %(count, totalCount)

    html = urllib.urlopen( url ).read()
    fixedHtml = ExtractDialogContent(html)

    fileName = outputPath + name+".html"
    writeFile = file(fileName, "w+")

    writeFile.writelines(fixedHtml)
    writeFile.close()


    


#extract txt name

#Temp Code
"""
tempUrlIndex = 1
tempHTML = urllib.urlopen( txtURL[tempUrlIndex] ).read()
tempHTMLTable = ExtractDialogContent( tempHTML )
tempFile = file("/home/zkun1983/Temp.html", "w+")
tempFile.writelines(tempHTMLTable)
tempFile.close()
"""
#print tempHTMLTable





