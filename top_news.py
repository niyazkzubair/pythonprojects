# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:27:24 2020

@author: nzubair
"""

import requests 
from bs4 import BeautifulSoup 
  
def news(): 
    # the target we want to open     
    url='https://news.google.com/news'
      
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        print("Successfully opened the web page") 
        print("The news are as follow :-\n") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     
        print (soup)
  
        # l is the list which contains all the text i.e news  
        l=soup.find("ul",{"class":"searchNews"}) 
        print (l)
      
        #now we want to print only the text part of the anchor. 
        #find all the elements of a, i.e anchor 
        for i in l.findAll("a"): 
            print(i.text) 
    else: 
        print("Error") 
          
news()