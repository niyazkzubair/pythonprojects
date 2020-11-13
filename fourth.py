# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 12:58:02 2018

@author: nzubair
"""
import pandas as pd
import time

##1
start = time.time()

df = pd.DataFrame(np.random.randint(0,12,size=(40, 5)),columns=['c1','c2','c3','c4','c5'])

end = time.time()

elapsed = end - start
print ("elapsed:",elapsed)

#display(df)

##2
start = time.time();

df = df.sort_values(by='c1')

end = time.time()
elapsed = end -start
print ("elapsed:",elapsed)


##3

start = time.time();

#df = df.sort_values(by=['c1','c2','c3','c4','c5'])

end = time.time()
elapsed = end -start
print ("elapsed:",elapsed)
#display(df)

val1 = 10
val2 = 5

new_df = df.where((df['c1'] > val2) & (df['c2'] < val1))
display(new_df)

new_df.to_csv("new_df.txt", sep='\t')
