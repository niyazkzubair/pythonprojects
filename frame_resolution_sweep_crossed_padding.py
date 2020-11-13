# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:14:02 2020

@author: nzubair
"""

fw_list = []

for i in range(1288,8093,200):
    print (i)
    for j in range(4,132,4):
        print ("\t",i+j)
        fw_list.append(i+j)
    