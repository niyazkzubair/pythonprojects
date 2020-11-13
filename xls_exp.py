# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:44:58 2020

@author: nzubair
"""


###Reference
#https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/
#https://www.journaldev.com/33306/pandas-read_excel-reading-excel-file-in-python
#https://datatofish.com/sort-pandas-dataframe/
#https://www.geeksforgeeks.org/iterating-over-rows-and-columns-in-pandas-dataframe/

import sys
import pandas 

pandas.options.display.max_rows = None;
pandas.options.display.max_columns = None
pandas.options.display.width = None
pandas.options.display.max_colwidth = 200

print ("-----------------------------------------------------------------------------------------------------------")
print ("--------------   REGRESSION DIFFERENCE REPORTER -- Version 1   ------------")
print ("-----------------------------------------------------------------------------------------------------------")
print ("[1][First regression Status]")
print ("[2][Test PASSed from First regression]")
print ("[3][Second regression Status]")
print ("[4][Test PASSed from Second regression]")
print ("[5][Status on following frames are common across both the regressions]")
print ("[6][Following frames are there only in first regression]")
print ("[7][Following frames are there only in second regression]")
print ("[8][Status of following frames differ between the regressions]")
print ("-----------------------------------------------------------------------------------------------------------")



#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
#regr_1 = sys.argv[1]
#regr_2 = sys.argv[2]
regr_1 = 'regr_3.xlsx'
regr_2 = 'regr_4.xlsx'

##[1]
print ("[1][First regression Status]\n")
#first_regr_report = pandas.read_excel('regr_1_bkup.xlsx', usecols="A:B")
first_regr_report = pandas.read_excel(str(regr_1), usecols="A,C")
#first_regr_report = pandas.read_excel('regr_1.xlsx', usecols=['TEST_CASE_NAME','STATUS'])
#first_regr_report = pandas.read_excel(files[0], usecols=['TEST_CASE_NAME','STATUS'])
print (first_regr_report)
print ("-----------------------------------------------------------------------------------------------------------")

##[2]
#Pandas(Index=0, Test='q2_por_adv_Q2_comp_ln94_0001_0001', Status='PASS')
#Pandas(Index=1, Test='q2_por_adv_Q2_comp_ln94_0000_0000', Status='TIMEOUT')
#Pandas(Index=2, Test='q2_por_adv_Q2_comp_ln96_0001_0001', Status='TIMEOUT')
print ("[2][Test PASSed from First regression]\n")
for i in first_regr_report.itertuples(): 
    if("PASS" in i[2]):
        print(i[1]) 
print ("-----------------------------------------------------------------------------------------------------------")

##[3]
print ("[3][Second regression Status]\n")
#second_regr_report = pandas.read_excel('regr_2_bkup.xlsx', usecols="A,B")
second_regr_report = pandas.read_excel(str(regr_2), usecols="A,C")
#second_regr_report = pandas.read_excel('regr_2.xlsx', usecols=['TEST_CASE_NAME','STATUS'])
#second_regr_report = pandas.read_excel(files[1], usecols=['TEST_CASE_NAME','STATUS'])
print (second_regr_report)
print ("-----------------------------------------------------------------------------------------------------------")

##[4]
print ("[4][Test PASSed from Second regression]\n")
for i in second_regr_report.itertuples(): 
    if("PASS" in i[2]):
        print(i[1]) 
print ("-----------------------------------------------------------------------------------------------------------")

##[5]
print ("[5][Status on following frames are common across both the regressions]\n")
df = first_regr_report.merge(second_regr_report, how = 'inner' ,indicator=False)
print (df)
print ("-----------------------------------------------------------------------------------------------------------")

##[6]
print ("[6][Following frames are there only in first regression]\n")
df1 = first_regr_report.merge(second_regr_report, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
#df1["REGR SET"] = "FIRST"
df1.insert(1,"REGR_SET","FIRST");
print (df1.drop('_merge',axis=1))
print ("-----------------------------------------------------------------------------------------------------------")

##[7]
print ("[7][Following frames are there only in second regression]\n")
df2 = first_regr_report.merge(second_regr_report, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']
#df2["REGR SET"] = "SECOND"
df2.insert(1,"REGR_SET","SECOND");
print (df2.drop('_merge',axis=1))
print ("-----------------------------------------------------------------------------------------------------------")


##[8]
print ("[8][Status of following frames differ between the regressions]\n")
#df= pandas.concat([first_regr_report,second_regr_report]).drop_duplicates(keep=False)
df= pandas.concat([df1,df2]).drop_duplicates(keep=False)
df = df.drop('_merge',axis=1)
df.sort_values(by=['TEST_CASE NAME','REGR_SET'],ascending=[True, True],inplace=True)
print (df)


#print(pandas.concat([first_regr_report,second_regr_report]).drop_duplicates(keep=False))

##[9]
##Write to file
df.to_csv(r'c:\Anaconda\pandas.txt', header=None, index=None, sep='\t', mode='a')
    
##Useful commands
#first_regr_report.equals(second_regr_report)
#first_regr_report.sort_values(by=['TEST_CASE_NAME'], inplace=True)
