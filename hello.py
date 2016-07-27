from Finder import process

import requests

url = "http://www.sameerkumar.website/"
test = requests.get(url)

f = open('/Users/sameer18051998/PycharmProjects/MyFirstPythonCharm/nullu.txt', 'r')
z=0
for x in iter(f.read().split()):
    if x=='Rao': z+=1
    print x
print 'overall- ',z
print x.__len__()
f.close()
