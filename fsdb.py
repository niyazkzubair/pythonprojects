# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:05:36 2020

@author: nzubair
"""
#https://pyfsdb.readthedocs.io/en/latest/index.html
#https://pypi.org/project/pyfsdb/
#https://www.isi.edu/~johnh/SOFTWARE/FSDB/

import pyfsdb
db = pyfsdb.Fsdb(out_file="myfile.fsdb")
db.out_column_names=('one', 'two')
db.append([4, 'hello world'])
db.close()

db = pyfsdb.Fsdb("myfile.fsdb")
print(db.column_names)
for row in db:
    print(row)