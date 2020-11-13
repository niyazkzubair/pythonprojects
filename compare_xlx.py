# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:53:57 2020

@author: nzubair
"""

import pandas as pd 
  
#Reading two Excel Sheets 
  
sheet1 = pd.read_excel(r'regr_1.xlsx') 
sheet2 = pd.read_excel(r'regr_2.xlsx') 
count = 0
mismatch = 0
  
# Iterating the Columns Names of both Sheets 
for i,j in zip(sheet1,sheet2): 
     
    #print ("I:",i," J:",j)
    # Creating empty lists to append the columns values     
    a,b =[],[] 
  
    # Iterating the row values of each column
    for m, n in zip(sheet1[i],sheet2[j]): 
        #print("M:",m," N:",n)
        # Appending values in lists 
        a.append(m) 
        b.append(n) 
        #print (a)
        #print (b)
        
     
    #print (a)
    #print (b)
    
    # Sorting the lists for the first column (Test name column), to see if the tests are same
    if(count == 0):
        a.sort() 
        b.sort() 
          
  
    # Iterating the list's values and comparing them 
    for m, n in zip(range(len(a)), range(len(b))): 
        print ("M:",m," N:",n)
        if a[m] != b[n]: 
            print('Column name : \'{}\' and Row Number : {}'.format(i,m)) 
            mismatch = mismatch + 1
        else:
            print ("Hai")
    
    if(count == 0 and mismatch == 0):
        print ("Test names matches between xls files")
    count = count + 1