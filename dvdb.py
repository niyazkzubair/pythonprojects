# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:07:51 2020

@author: nzubair
"""

#https://docs.sqlalchemy.org/en/13/orm/tutorial.html
#https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///sim.sqlite', echo = True)
meta = MetaData()


#Only during creation
simulation = Table(
   'simulation', meta, 
   Column('Entry_id', Integer, primary_key = True), 
   Column('Date', String), 
   Column('Project', String), 
   Column('Type', String), 
   Column('Simulator', String), 
   Column('Tool', String), 
   Column('Version', String), 
   Column('Found_at', String), 
   Column('Issue_category', String), 
   Column('Issue_details', String), 
   Column('Fix_details', String), 
   Column('More_info', String), 
)

meta.create_all(engine)

###Insert entry
#ins = simulation.insert().values(
#    Entry_id = '1',
#    Date = 'wer',
#    Project = 'MakenaV2',
#    Type = 'memory',	
#    Simulator = 'VCS',
#    Tool = 'XXX',
#    Version = '6.6f',	
#    Found_at = 'TOP',
#    Issue_category = 'run_time',
#    Issue_details =	'ERROR',
#	 Fix_details = 'Run_on',
#    More_info = 'XXX'
#    )

conn = engine.connect()

#result = conn.execute(ins)


#Print the database
s = simulation.select()
result = conn.execute(s).fetchall()
for row in result:
   print (row)
   
#Update one attribute
stmt=simulation.update().where(simulation.c.Issue_details=='UPDATE').values(Issue_details='ERROR: The MODELTECH VERSION: 6.6f is not valid')
conn.execute(stmt)

s = simulation.select()
result = conn.execute(s).fetchall()
for row in result:
   print (row)    
