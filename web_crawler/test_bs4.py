from bs4 import BeautifulSoup
import requests, re

url = 'http://m.kdslife.com/club/'
# get whole HTTP response
response = requests.get(url)
# args[0] is HTML document, args[1] select LXML parser. returned BeautifulSoup object
soup = BeautifulSoup( response.text, 'lxml')
print soup.name
# [document]'
print type(soup)
# <class 'bs4.BeatifulSoup'>

"""
# BeutifulSoup --> Tag 
# get the Tag object(title)
res = soup.title
print res
# <title>KDS Life</title>

res = soup.title.name
print res
# title

# attribules of a Tag object
res = soup.section
print type(res)
# <class 'bs4.element.Tag'>

print res['class']
# ['forum-head-hot', 'clearfix']

# All the attributes of section Tag object, returned a dict
print res.attrs
#{'class': ['forum-head-hot', 'clearfix']}


# NavigableString object describes the string in Tag object
res = soup.title
print res.string
# KDS Life
print type(res.string)
# <class 'bs4.element.NavigableString'>
"""

"""
# Comment, is a special NavigableString object
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
print type(comment)
# <class 'bs4.element.Comment'>
"""

"""
# filter, returned a matching list
# returned [] if matching nothing
title = soup.find_all('title')
print title
#[<title>Google</title>]

res = soup.find_all('div', 'topAd')
print res

# find all the elements whose id is 'gb-main'
res = soup.find_all(id='topAd')
print res
#[<div id="topAd">...</div>]

# find all the elements with 'img' tag and 'src' attribute matching the specific pattern
res = soup.find_all('img', src=re.compile(r'^http://club-img',re.I))
print res
# [<img src="http://club-img.kdslife.com/attach/1k0/gs/a/o41gty-1coa.png@0o_1l_600w_90q.src"/>,
#...]
"""



"""
# css selector
# select those whose tag's id = wrapperto
res = soup.select('#wrapperto')
print res
# [<div class="swiper-wrapper clearfix" id="wrapperto"></div>]

# select those 'img' tags who have 'src' attribute
res = soup.select('img[src]')
print res
#[<img alt="" src="http://icon.pch-img.net/kds/club_m/club/icon/user1.png"/>, <im
#g src="http://club-img.kdslife.com/attach/1k0/gs/a/o41gty-1coa.png@0o_1l_600w_90q.src"/>]

# select those 'img' tags whose 'src' attribute is 
res = soup.select('img[src=http://icon.pch-img.net/kds/club_m/club/icon/user1.png]')
print res
# [<img alt="" src="http://icon.pch-img.net/kds/club_m/club/icon/user1.png"/>]
"""


# get_text()
markup = '<a href="http://example.com/">\n a link to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup,'lxml')
res = soup.get_text()
print res
#  a link to example.com

res = soup.i.get_text()
print res
# example.com

# .stripped_string
res = soup.stripped_strings
print list(res)
# [u'a link to', u'example.com']