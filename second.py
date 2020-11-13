# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:40:22 2018

@author: nzubair
"""

print("Hello")

import pandas as pd
names1880 = pd.read_csv('C:\Venus\Python_Data_Analysis\yob1880.txt', names=['name', 'sex', 'births'])
display(names1880)  
display(names1880.groupby('sex').births.sum())