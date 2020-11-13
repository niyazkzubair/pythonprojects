# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:25:38 2020

@author: nzubair
"""

import pandas as pd
import tabula
file = "AC_STATEMENT_1472XXXXXX7645_19OCT2019_25OCT2019_26102019101190.pdf"
#path = 'enter your directory path here'  + file
path = file


df = tabula.read_pdf(path, pages = '1', multiple_tables = True)
print(df)