# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:52:34 2020

@author: nzubair
"""

print ("Hello World");


##Numeric
a  = 123
b  = 2 + 3j
c  = 4.5
d = a+b+c

##String
s1 = "qwert"
s2 = 'asdf'
print ("Size of s1 is: ",len(s1))
str1 = 'Python is Nice'

if(str1[0] == 'P'):
    print ("FIrst alphabet is P")


if('Ni' in 'Python is Nice'):
    print ("FOUND in STRING")

############################## List
array_list_a1 = [4,"abc",6.7,(56,"tyu",3+4j)]
##appending to list
array_list_a1.append("ert")
##adding a new item to list
array_list_a1 = array_list_a1 + [67,"ghj"]
##Below is possible
array_list_a1[3] = 34

#############################  Tuple
tuple_t1 = (34,"zxc",5.6)
tuple_t1 = tuple_t1 + (2,[1,"456",5.6])
##Below are not possible as tuple is immutable
#tuple_t1[4] = 34
#tuple_t1.append(45)

#############################  Dictionary
dict_1 = {'Language':"Python",1:2.0}

for i in dict_1: # Returns keys
    print (type(i))
    print ("i: ",i)
    print ("dict_1[i]: ",dict_1[i])
    
for i in dict_1.values(): #Returns values
    print ("Value: ",i)
    
for i,j in dict_1.items(): #Returns (key, value) pair
    print (i,j)

dict_2 = dict_1 #pointer, so all changes in dict will be reflected in dict_2
dict_3 = dict_1.copy() #Copies values

#Adding a new item to dictionary
dict_1['Popularity'] = "Good"
abc = dict_1.keys()

##Check one key exists
if 'Language' in dict_1:
    print ("Language is one key in the dictionary")
    
#pop(), popitem(), del, clear()

##Nested dictionary
nested_dict = {
    'India' : {'Continent':'Asia','Capital':'Delhi'},
    'France': {'Continen':'Europe','Capital':'Paris'}}

print(nested_dict.keys())

################################# Other For loops
##1

count = 0
for letter in 'Python is Nice':
    print (letter)
    if(letter == 'i'):
        count += 1

##2
print ("\n\n")
for i in tuple_t1:
    print (i)

##3
print ("\n\n")
for p in range(0,10):
    print (p)
