# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:30:32 2020

@author: nzubair
"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://feeds.reuters.com/~r/Reuters/worldNews/~3/fM4LzcQzTgU/china-says-peak-of-coronavirus-epidemic-has-passed-idUSKBN20Z0WB'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print (soup.find_all('p'))