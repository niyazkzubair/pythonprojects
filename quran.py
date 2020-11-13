# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:32:19 2020

@author: nzubair
"""

#http://textminingthequran.com/data/quranic-corpus-morphology-0.4.txt
#http://corpus.quran.com/download/
#http://abdulbaqi.io/2019/01/19/quranic-roots-pandas/
#http://abdulbaqi.io/2019/01/15/quranic_roots/
#https://pypi.org/project/pyquran/
#http://abdulbaqi.io/tag/technology/


#Chronological order of surahs
#https://www.webcitation.org/query?url=http://www.bombaxo.com/chronsurs.html&date=2011-05-13
#Lots of info about Quran
#https://www.webcitation.org/query?url=http://tanzil.net/pub/ebooks/History-of-Quran.pdf&date=2011-05-13
#An Introduction to the sciences of Quran
#https://archive.org/details/IntroductionToSciencesOfTheQuran/page/n319/mode/2up
#Order of revelartion of surahs
#https://www.webcitation.org/query?url=http://www.bombaxo.com/chronsurs.html&date=2011-05-13
#Word2vec
#https://www.freecodecamp.org/news/how-to-get-started-with-word2vec-and-then-how-to-make-it-work-d0a2fca9dad3/

import sys
import pandas  as pd
import re
from datetime import datetime


start_time = datetime.now()
ayath_root = pd.DataFrame(columns=['AYATH','ROOT'],index=range(1,1))
t = pd.DataFrame(columns=['AYATH','ROOT'],index=range(1,1))

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str
  
# Driver code 

count = 0;
for line in open('quranic-corpus-morphology-0.4.txt'):
    if('ROOT' in line and count < 50000):
        ayath =  line.split(')')
        portions = line.split('|')
        
        count = count + 1
        
        for part in portions:
            if ('ROOT' in part):
                #print (ayath[0],"----",part)
                                
                
                portions = part.split('ROOT:')
                root_word = portions[1]
                
                portions = ayath[0].split('(')
                ayath_number = portions[1]
                #print ("FIRST :",ayath_number)
                
                portions = re.split(':',ayath_number,2)
                temp = portions[:2]
                ayath_short = portions[0],":",portions[1]
                ayath_short_s = ''.join(ayath_short)
                ayath_short_final = ayath_short_s.replace(", :, ",':')
                
             
                
                t = pd.DataFrame({'AYATH':[ayath_short_final],'ROOT':[root_word],'FLAG':0})
                ayath_root = pd.concat([ayath_root,t],ignore_index=True)

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 100)

ayath_root_uniquified = ayath_root.drop_duplicates()
##[1] -- AYATH_ROOT data frame
#print (ayath_root_uniquified)
print ("ORIGINAL AYATH_ROOT_COUNT :",ayath_root['AYATH'].count())
print ("UNIQIFIED AYATH_ROOT_COUNT :",ayath_root_uniquified['AYATH'].count())

##[2] -- Write AYATH with ROOT counts to file
print ("AYATH with ROOT counts: ")
ayath_flow = (ayath_root_uniquified['AYATH'].value_counts().reset_index())
ayath_flow.columns = ['AYATH','COUNT']
#print (ayath_flow)
ayath_flow.to_csv("ayaths.txt")

ayath_root_sorted_with_occcurance_count = pd.DataFrame(columns=['AYATH','ROOT'],index=range(1,1))
for i,r in ayath_flow.iterrows():
    #print(r['COUNT'])
    v = (ayath_root_uniquified.loc[ayath_root_uniquified['AYATH'] == r['AYATH']])
    ayath_root_sorted_with_occcurance_count = pd.concat([ayath_root_sorted_with_occcurance_count,v],ignore_index=True)
    
#print(ayath_root_uniquified)
#print(ayath_root_sorted_with_occcurance_count)

ayath_root_uniquified = ayath_root_sorted_with_occcurance_count

    
##[3] -- ROOT word counts 
#print ("ROOT COUNTS: ")
#print (ayath_root['ROOT'].value_counts())

##[4] -- print all ayas with more than x ROOT words
#print (ayath_flow[ayath_flow.COUNT > 10])
temp_1 = ayath_flow[ayath_flow.COUNT > 10]
temp_1.to_csv("ayath_with_occur_count.txt")
print ("NO. OF AYATHS WITH GREATER THAN x ROOT WORDS:",temp_1['AYATH'].count())


ayath_sorted_root = ayath_root.sort_values(by=['AYATH','ROOT'], ascending=True)
ayath_sorted_root_drop_duplicates = ayath_sorted_root.drop_duplicates(ignore_index=True)

#print (ayath_sorted_root_drop_duplicates)
print ("COUNT1: ",ayath_sorted_root_drop_duplicates['AYATH'].count())

temp_2 = ayath_sorted_root_drop_duplicates

#for index,row in ayath_sorted_root_drop_duplicates.iterrows():
#    for i,r in temp_2.iterrows():
#        if(row['AYATH'] != r['AYATH'] and row['ROOT'] == r['ROOT'] and r['FLAG'] == 0):
#            temp_2.drop(i,inplace=True)
#            #print (i)
#        else:
#            temp_2.loc[i,'FLAG'] = 1;
#    ayath_sorted_root_drop_duplicates = temp_2
    

for idx,row in ayath_sorted_root_drop_duplicates.iterrows():
    temp_2.drop(temp_2[(temp_2.index > idx) & (temp_2['AYATH'] != row['AYATH']) & (temp_2['ROOT'] == row['ROOT'])].index,inplace=True)
            
#print(temp_2)
temp_3 = temp_2.drop_duplicates()
#print (temp_3)
print ("COUNT2: ",temp_3['AYATH'].count())


only_ayaths = temp_3['AYATH'].to_frame()
only_ayaths_wo_duplicates = only_ayaths.drop_duplicates()
only_ayaths_wo_duplicates_sorted = only_ayaths_wo_duplicates.sort_values('AYATH')

#print (only_ayaths_wo_duplicates_sorted)
print ("COUNT3: ",only_ayaths_wo_duplicates_sorted.count())

learn_these_ayaths = pd.DataFrame(columns=['AYATH','COUNT'],index=range(1,1))

for i,r in only_ayaths_wo_duplicates_sorted.iterrows():
    d = ayath_flow.loc[ayath_flow['AYATH'] == r['AYATH']]
    learn_these_ayaths = pd.concat([learn_these_ayaths,d],ignore_index=True)

learn_these_ayaths_sorted = learn_these_ayaths.sort_values(by=['COUNT'],ascending=False)
#print(learn_these_ayaths_sorted)
learn_these_ayaths_sorted.to_csv("learn_these_ayaths.txt")

incremental_root_words = pd.DataFrame(columns=['AYATH','ROOT'],index=range(1,1))
for i,r in learn_these_ayaths_sorted.iterrows():
    e = ayath_root_uniquified.loc[ayath_root_uniquified['AYATH'] == r['AYATH']]
    incremental_root_words = pd.concat([incremental_root_words,e],ignore_index=True)
    
#print((incremental_root_words.drop_duplicates(subset='ROOT')).sort_values(by=['ROOT']))
incremental_root_words = (incremental_root_words.drop_duplicates(subset='ROOT'))
#print(incremental_root_words)
print(incremental_root_words['AYATH'].value_counts())

#for i,r in incremental_root_words.iterrows():
    

end_time = datetime.now()
print('Time Taken by the program: {}'.format(end_time - start_time))
sys.exit()


#########################################################################################################################################
################ STOPPING HERE #########################
#########################################################################################################################################

#print (ayath_root)
ayath_sorted_root = ayath_root.sort_values(by=['ROOT'], ascending=True)
#ayath_sorted_root = ayath_root.sort_values(by=['AYATH','ROOT'], ascending=True)
#print (ayath_sorted_root)

ayath_root_1 = ayath_sorted_root.drop_duplicates()

only_ayaths = ayath_root_1['AYATH']
#print (only_ayaths)

only_ayaths_wo_duplicates = only_ayaths.drop_duplicates()
only_ayaths_wo_duplicates_sorted = only_ayaths_wo_duplicates.sort_values()

#print(only_ayaths_wo_duplicates_sorted)
print("Total ayath count :",only_ayaths_wo_duplicates_sorted.count())

only_roots = ayath_root_1['ROOT']
#print (only_roots)

only_roots_wo_duplicates = only_roots.drop_duplicates()
only_roots_wo_duplicates_sorted = only_roots_wo_duplicates.sort_values()
#print (only_roots_wo_duplicates_sorted)
print("Total root count ",only_roots_wo_duplicates_sorted.count())


index_array = only_roots_wo_duplicates_sorted.index
index_array_sorted = index_array.sort_values()

print ("AYATH INDEX: ",index_array_sorted)


p = pd.DataFrame(columns=['AYATH','ROOT'],index=range(1,1))
q = pd.DataFrame(columns=['AYATH','ROOT'],index=range(1,1))


for index,row in ayath_root.iterrows():
    for entry in index_array_sorted:
        if(index == entry):
            #print (index)
            #print (index," ",row['AYATH']," ",row['ROOT'])
            p = pd.DataFrame({'AYATH':[row['AYATH']],'ROOT':[row['ROOT']]})
            q = pd.concat([q,p],ignore_index=True)
            
#print(q)

q_only_ayaths = q['AYATH']
q_only_ayaths_sorted = q_only_ayaths.sort_values()
q_only_ayaths_sorted_wo_duplicates = q_only_ayaths_sorted.drop_duplicates()

print ("UNIQUE AYATHS: ")
print (q_only_ayaths_sorted_wo_duplicates)
print ("UNIQUE AYATH COUNT: ",q_only_ayaths_sorted_wo_duplicates.count())

