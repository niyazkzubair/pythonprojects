# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:10:23 2020

@author: nzubair
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_url = 'http://bit.ly/2cLzoxH'
#gapminder = pd.read_csv(data_url)
gapminder = pd.read_csv("pop_data.txt")

print(gapminder.head(3))

df1 = gapminder[['continent', 'year','lifeExp']]
print(df1)


plt.figure(figsize=(10,5))
heatmap1_data = pd.pivot_table(df1, values='lifeExp', 
                     index=['continent'], 
                     columns='year')

sns.heatmap(heatmap1_data, cmap="YlGnBu",annot=True)

