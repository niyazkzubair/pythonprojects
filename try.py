# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:07:51 2020

@author: nzubair
"""

#https://docs.sqlalchemy.org/en/13/orm/tutorial.html
#https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import text
from sqlalchemy.sql import select
from sqlalchemy import and_

engine = create_engine('sqlite:///abc.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

##Inserting entries
#ins = students.insert()
#ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
#conn = engine.connect()
#result = conn.execute(ins)

#Inserting entried in bulk
#conn.execute(students.insert(), [
#   {'name':'Rajiv', 'lastname' : 'Khanna'},
#   {'name':'Komal','lastname' : 'Bhandari'},
#   {'name':'Abdul','lastname' : 'Sattar'},
#   {'name':'Priya','lastname' : 'Rajhans'},
#])

#Fetching entries
#s = students.select()
s = students.select().where(students.c.id>2)
conn = engine.connect()
result = conn.execute(s)

for row in result:
   print (row)