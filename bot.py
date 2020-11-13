# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 01:05:51 2020

@author: nzubair
"""

import requests
from bs4 import BeautifulSoup
#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Xi8-bcgzaUk")
page
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())