# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:49:21 2020

@author: nzubair
"""
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import time

def get_news_dailymail():
    
    # url definition
    url = "https://www.dailymail.co.uk"
    
    # Request
    r1 = requests.get(url)
    r1.status_code

    # We'll save in coverpage the cover page content
    coverpage = r1.content

    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html5lib')

    # News identification
    coverpage_news = soup1.find_all('h2', class_='linkro-darkred')
    len(coverpage_news)
    
    number_of_articles = 5

    # Empty lists for content, links and titles
    news_contents = []
    list_links = []
    list_titles = []

    for n in np.arange(0, number_of_articles):

        # Getting the link of the article
        link = url + coverpage_news[n].find('a')['href']
        list_links.append(link)

        # Getting the title
        title = coverpage_news[n].find('a').get_text()
        list_titles.append(title)

        # Reading the content (it is divided in paragraphs)
        article = requests.get(link)
        article_content = article.content
        soup_article = BeautifulSoup(article_content, 'html5lib')
        body = soup_article.find_all('p', class_='mol-para-with-font')

        # Unifying the paragraphs
        list_paragraphs = []
        for p in np.arange(0, len(body)):
            paragraph = body[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = " ".join(list_paragraphs)

         # Removing special characters
        final_article = re.sub("\\xa0", "", final_article)
        
        news_contents.append(final_article)
        

    # df_features
    df_features = pd.DataFrame(
         {'Content': news_contents 
        })

    # df_show_info
    df_show_info = pd.DataFrame(
        {'Article Title': list_titles,
         'Article Link': list_links,
         'Newspaper': 'Daily Mail'})
    print(df_features)
    print(df_show_info)
    
    return (df_features, df_show_info)


start = time.time()
x, y = get_news_dailymail()
end =time.time()
te = end-start
print("The time elapsed is %f seconds" %(te))