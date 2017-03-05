import re
import urllib
checkURL = "http://fallout.wikia.com/wiki/188CivilianHopeful.txt"



htmlObj = urllib.urlopen(checkURL)


html = htmlObj.read()


def MultiFind(reg, text):
    return re.findall(reg, text, flags=re.DOTALL+re.MULTILINE)



reg = "np-table-dialogue\">(.*</table>)"


data = MultiFind(reg, html)

print data
