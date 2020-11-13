# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:21:03 2020

@author: nzubair
"""

import pandas as pd

'''
data_url = 'http://bit.ly/2cLzoxH'
# read data from url as pandas dataframe
f = pd.read_csv(data_url)
print(f.head(3))
# select two columns
f1 = f[['continent','pop']]
f1.head()
'''

f = pd.read_csv('JIRA_Hardware.csv')
niyaz = f['Reporter'] == "K.Zubair, Niyaz"
harshit = f['Reporter'] == "Patel, Harshit"

f1 = f[niyaz | harshit][["Reporter","Type","Component/s"]]
print("TB Issues count :",f1[f1["Type"] == "TB"].count())
print("CSIM Issues count :",f1[f1["Type"] == "Systems"].count())
print("RTL Issues count :",f1[f1["Type"] == "RTL"].count())