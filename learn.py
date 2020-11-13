# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:23:05 2020

@author: nzubair
"""

for i in range(128):
    if i%4 == 0:
        print ("val_",i,"=",i)
    else:
        if i%4 == 1:
            print ("val_",i,"_",i+2,"=[",i,":",i+2,"]")