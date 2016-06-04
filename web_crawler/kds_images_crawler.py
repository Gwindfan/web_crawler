import re
import os
import requests
import time
from bs4 import BeautifulSoup

# mobile KDS club portal
url = 'http://m.kdslife.com/club/'
print "Now downloading today's pictures from :" + url
# local directory for storing downloaded image files
start = time.time()
nowInSecs= int(round(start))
dir = 'D:\\Python\\spider\\' + str(nowInSecs)

# get and store HTTP response
response = requests.get(url)


# Crawling images
# use LXML parser parsing HTML content
soup = BeautifulSoup(response.text, 'lxml')
rePattern = '^http://club-img'
# returned a list of Tag objects
res = soup.find_all('img', src=re.compile(rePattern, re.I))
# get url of each image and kept in a list
imageUrlList = []

for one in res :
    imageUrlList.append(one['src'])    

print count

# save in local file system
if not os.path.isdir(dir) : 
    os.mkdir(dir)

numerator = 1    
for url in  imageUrlList :
    r = requests.get(url)
    pic = r.content
    file = dir + '\\' + str(numerator) + '.jpeg'
    fh = open(file, 'wb')
    fh.write(r.content)
    fh.close()
    numerator += 1

    
# statistics
end = time.time()
duration = end - start
print "Downloaded " + str(numerator) + ' pictures and stored in ' + dir, 'Cost {:.2f} seconds'.format(duration)