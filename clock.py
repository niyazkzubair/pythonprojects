from bs4 import BeautifulSoup as bs
from pytube import YouTube
from splinter import Browser

import time

browser = Browser('chrome', headless=False)  # set headless to False to see browser
browser.visit('https://www.youtube.com/results?search_query=clocks')  # change query to your search

num_pages = 5
# sleeps to wait for page loads
time.sleep(2)
for i in range(num_pages):
    time.sleep(5.0)

    browser.execute_script("window.scrollBy(0, window.innerHeight * 2);")

page = browser.html.encode()
soup = bs(page, 'html.parser')
vids = soup.findAll('a', attrs={'class':'yt-simple-endpoint style-scope ytd-video-renderer'})
browser.quit()

columns = ['id', 'url', 'title']
videolist =[]
for v in vids:
    try:
        tmp = {'id': v['href'].split('?v=')[1],
               'url': 'https://www.youtube.com' + v['href'],
               'title': v['title']}
        videolist.append(tmp)
    except:
        continue

for item in videolist:
    tube = YouTube(item['url'])
    filepath = tube.streams.first().download()
    print(filepath)