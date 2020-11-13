# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 03:05:30 2020

@author: nzubair
"""
#!/usr/bin/env python
# coding: utf-8

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import os

##Copied below code for news.py
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import urllib.request
import nltk

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
 
def read_article(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    #print (filedata)
    try:
        article = filedata[0].split(". ")
        sentences = []

        for sentence in article:
            ###Print the sentence below
            #print(sentence)
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
        sentences.pop() 
    
    except IndexError:
        sentences = []
    
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(file_name, top_n=5,news_count=1):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Read text anc split it
    sentences =  read_article(file_name)
    #print ("Step 1")

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    #print ("Step 2")

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)
    #print ("Step 3")

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True) 
    #print ("Step 4")   
    #Below is a very useful step
    #print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    for i in range(top_n):
      try:
          summarize_text.append(" ".join(ranked_sentence[i][1]))
      except IndexError:
          summarize_text.append(" ".join(" "))
    #####Print below to see the news
    #print (summarize_text)
    # Step 5 - Offcourse, output the summarize texr
    print("Summarized News: [", news_count,"] -",". ".join(summarize_text))
    #print (word_count(join(summarize_text)))    
##Copy ended

#news_url="https://news.google.com/news/rss"
#news_url=["http://feeds.bbci.co.uk/news/world/rss.xml","http://feeds.bbci.co.uk/news/technology/rss.xml","http://feeds.reuters.com/Reuters/worldNews"]
#news_url=["http://feeds.bbci.co.uk/news/world/rss.xml"]
news_url=["http://feeds.bbci.co.uk/news/technology/rss.xml"]
news_url=["http://feeds.reuters.com/Reuters/worldNews"]
news_url=["http://feeds.bbci.co.uk/news/rss.xml"]
news_url=["http://feeds.bbci.co.uk/news/business/rss.xml"]


news_url=["https://news.google.com/news/rss",
          "http://feeds.bbci.co.uk/news/world/rss.xml",
          "http://feeds.bbci.co.uk/news/technology/rss.xml",
          "http://feeds.bbci.co.uk/news/rss.xml",
          "http://feeds.bbci.co.uk/news/business/rss.xml"
          ]

#news_url=["https://news.google.com/news/rss"]
news_url=["http://feeds.bbci.co.uk/news/world/rss.xml",
          "https://news.google.com/news/rss"
          ]

news_count = 1;
feed_count = 0
for ijk in news_url:
    print ("NEWS LINK --",ijk)
    Client=urlopen(ijk)
    xml_page=Client.read()
    Client.close()
    print ("XML:",xml_page)
    
    feed_count = feed_count + 1


    soup_page=soup(xml_page,"xml")
    print ("[[[[[[[[[[[[[[[[SOUP]]]]]]]]]]]]]]:",soup_page)
    
    
    #try:
    news_list=soup_page.findAll("item")
        #print (news_list)
    #except AttributeError:
    #    print ("Skipped -- AttributeError")
    # Print news title, url and publish date
    for news in range(1,5):
    #for news in range(17,20):
    #for news in range(1,len(news_list)):
        #Get the link to the news
        #print("[[]]",news_list[news].title.text)
        #print(news_list[news].link.text)
        #print(news.description.text)
        #print(news.pubDate.text)
        #print(news.source)
        
        #Read the webpage
        response = requests.get(news_list[news].link.text)
        #soup = BeautifulSoup(response.text, 'html.parser')
        soup = BeautifulSoup(response.text, 'html5lib')
        
        entry =  (soup.find_all('p'))
        #print ("OLD --:",entry)
        
        #new_entry = re.sub('<p.*class.*</p>, ','',str(entry))
        entry_list = str(entry).split('<p>')
        #print ("NEW --:",entry_list)
        pqr='';
        for ijk in entry_list:
            if(("[NEWS]" not in ijk) and ("aria-hidden" not in ijk)):
                rst = re.sub('</p>','',ijk)
                rst = re.sub('<a.*">','',rst)
                rst = re.sub('</a>','',rst)
                rst = re.sub('<p.*">','',rst)
                #print (rst)
                pqr = pqr + str(rst)
        ######Print the news
        #print (pqr)
        
   
        if(os.path.exists("single_news.txt")):
            file1 = open("single_news.txt","a")
            file1.close()
        file1 = open("single_news.txt","a")
        try:
            file1.write(pqr)
        except UnicodeEncodeError:
            print ("Skipped -- UnicodeEncodeError")
        file1.close()
        
        ########### SEARCH SPECIFIC NEWS
        if(("corona" not in str(pqr)) and ("Corona" not in str(pqr))):
        #if(1):
            print ("\n")
            print("[[",news_count,"]]",news_list[news].title.text)
            print(news_list[news].link.text)
            #generate_summary("single_news.txt", 2,news_count)
            news_count = news_count + 1
            print("-"*100)
        #################################
            
        #Remove the single news file
        os.remove("single_news.txt")
        
        #print (soup.select("p#class"))
        #print (list(soup.children))
        #for item in list(soup.children):
        #    print (type(item))
        #print (soup.prettify())
        #print (soup.get_text())
    soup_page.clear()
        
print ("total news",news_count)