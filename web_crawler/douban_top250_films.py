from pandas import DataFrame
import requests
from bs4 import BeautifulSoup
import sys, re
reload(sys)
sys.setdefaultencoding('utf-8') # in case of setting with acsii, which gets UnicodeEncodeError

urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
your_cookie = 'get your cookie value'
headers = {
    'User-Agent' : 'Mozilla/5.0',
    'Cookie' : your_cookie
}
# global variables definition
file = 'D:\\Python\\web_crawler\\top250.csv'
titles = []
images = []
ratings = []
stars = []

def crawlFilms (url, headers) :
    response = requests.post(url, headers=headers, verify=False)
    # Check page encoding
    print 'Web page encoded with ', response.encoding
    #print 'Whole page: 'response.content
    soup = BeautifulSoup( response.text, 'lxml')
    # css selector
    title_list = soup.select('ol.grid_view > li > div.item > div.info > div.hd > a')
    image_list = soup.select('ol.grid_view > li > div.item > div.pic > a > img')
    rating_list = soup.select('ol.grid_view > li > div.item > div > div > div > span.rating_num')
    star_list = soup.select('ol.grid_view > li > div.item > div > div > p')
    for t, i, s, r in zip(title_list, image_list, star_list ,rating_list) :
        titles.append(t.get_text(strip=True))
        images.append(i.get('src'))
        ratings.append(r.get_text().strip())
        stars.append(s.get_text().strip())
      
# main
for url in urls:
    crawlFilms(url, headers)
# dict for DataFrame()
content_dict = {u'Film name' : titles, u'Image link' : images, u'Starring' : stars, u'Score' : ratings }
cols = []
# get columns to list in the csv file
for key in content_dict.keys() :
    cols.append(unicode(key))
print cols
frame = DataFrame(content_dict, columns = cols)
# starting index with 1 when writing pandas
frame.index += 1
frame.to_csv(file, index = True)

# Failures toubleshooting
# 1# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-5: ordinal not in range(128)
# Reason: You cannot decode Unicode data, it is already decoded. Python decode unicode implicitly. 
# Solution: sys.setdefaultencoding('utf-8'). default to 'ascii' in Python 2, to 'utf-8' in Python 3