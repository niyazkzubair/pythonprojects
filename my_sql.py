# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:27:22 2020

@author: nzubair
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nzubair",
  passwd="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")