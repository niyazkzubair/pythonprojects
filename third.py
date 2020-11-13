# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:26:13 2018

@author: nzubair
"""

#Heirarchical indexing
#"Python for data analysis" -- Page 147

import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(10),index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

display(data)

df = pd.DataFrame(#np.random.rand(4, 10),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['Test name','FW','FH','GMO','SH','SV','PRG_PIX_X','PRG_PIX_Y','PRG_BW','PRG_BH'])

display(df)

print ("\n\nHello_1")

#df.loc[('a','1')]['Test name'] = "Test_0"

df.at['b','Test name'] = "Test_1"

display(df)

print ("\n\nHello_2")

df.loc['a','GMO'] = -16

display(df.keys())

print ("Hello_3")

#df.set_index(['Test name'], inplace=True)


display(df)



