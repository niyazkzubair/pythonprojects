# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:12:20 2020

@author: nzubair
"""

# Python program to generate WordCloud 
  
# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
  

df = pd.read_csv(r"HMS_survey.csv", encoding ="latin-1") 
  
comment_words = ' '
stopwords = set(STOPWORDS) 


  
# iterate through the csv file 
for val in df.LIKE: 
      
    # typecaste each val to string 
    val = str(val) 
  
    # split the value 
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
          
    for words in tokens: 
        comment_words = comment_words + words + ' '

comment_words = comment_words.replace("nan",'')
comment_words = comment_words.replace("nil",'')
comment_words = comment_words.replace("dont",'')
  
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 50).generate(comment_words)


#https://www.geeksforgeeks.org/generating-word-cloud-python/
#https://www.geeksforgeeks.org/generating-word-cloud-in-python-set-2/
#https://www.datacamp.com/community/tutorials/wordcloud-python
# plot the WordCloud image     
                   
plt.figure(figsize = (8, 8), facecolor = None) 
#plt.imshow(wordcloud, interpolation='bilinear') 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 