# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:01:02 2020

@author: nzubair
"""

import sys
import pandas as pd

df = pd.DataFrame(columns = ['TEST_NAME','RAM_NUMBER'])
df = pd.read_csv("test_list.csv")

df = df.drop_duplicates(subset='RAM_NUMBER', keep="first")

df.to_csv("test_list_uniq.csv")

print (df['TEST_NAME'].unique())

s1 = list(df['TEST_NAME'].unique())

print("NUMBER OF OPTIMIZED FRAMES :",len(s1))


