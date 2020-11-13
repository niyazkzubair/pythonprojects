# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:56:24 2020

@author: nzubair
"""

import sys
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns


pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 100)

#regr = pd.read_csv("FE_RTL_REGR_RESULT.txt")

regr = pd.DataFrame(columns = ['TEST_NUMBER','TEST','TEST_TYPE','SEED','FAILURES','STATUS','LOG_PATH'])

low_end  = [987654321, 246813579, 135792468, 123456789,      0,      1,          2,              11,         51,             101,            501]
high_end = [987654321, 246813579, 135792468, 123456789,      0,      1,          10,             50,         100,            500,            1000000]
cat      = ['CSIM_CRASH', 'RAND_ERR', 'TIMEOUT', 'TB_ISSUE','PASS', 'ONE_ERROR', '2_TO_10_ERRORS',    '11_TO_50_ERRORS', '51_TO_100_ERRORS',   '101_TO_500_ERRORS',  'ABOVE_500_ERRORS' ]



#Read the input file and write in to dataframe
#for line in open('REGR_2_INPUT.txt'): #FG
for line in open('FE_REGR_819_1030AM.txt'): #FE_RANDOM_REGR
#for line in open('FG_REGR_521_0400PM.txt'): #FE_RANDOM_REGR
    #print (line)
    
    entries = line.split(":")
    test_log_path = entries[0];
    entries = line.split("/")
    for i in entries:
        if (('test_fg' in i) or ('test_lcu' in i)) :
            test_details = i.split('.')
            test_number = test_details[0]
            test_name = test_details[1]
            test_seed = test_details[2]
    
    if("UVM_ERROR" in line):
        entries = line.split(":")
        test_num_errors = int(entries[2])
        
    if("UVM_FATAL" in line):
        test_num_errors = 123456789;
        if("FE CSIM_FAIL" in line):
            test_num_errors = 987654321;
        if("Interface TIMEOUT" in line):
            test_num_errors = 135792468;
        if("Randomization" in line):
            test_num_errors = 246813579;
            #print (line)
    
    ##Deriving test type from test name
    test_type = []
    type_flag = 0
    if('db' in line):
        test_type.append('DB')
        type_flag = 1
    if('cdef' in line):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('CDEF')
        type_flag = 2
    if('lr' in line):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('LR')
        type_flag = 3
    if('upscale' in line):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('UPSCALE')
        type_flag = 4
    if('tile' in line):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('TILE')
        type_flag = 5
    if('padded' in line):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('PADDED')
        type_flag = 6
    
    test_type_final = ''.join(test_type)
    #####################################
    
    
    for i in range(len(low_end)):
        if(test_num_errors >= low_end[i] and test_num_errors <= high_end[i]):
            test_err_type = cat[i]
            break

    regr.loc[-1] = [test_number,test_name,test_type_final,test_seed,test_num_errors,test_err_type,test_log_path]
    regr.index = regr.index + 1

writer = pd.ExcelWriter('output.xlsx')    
regr = regr.drop_duplicates() 



#Operations on dataframe
regr_sorted = regr.sort_values(by='FAILURES')
regr_sorted = regr_sorted.reset_index(drop=True)

regr_sorted.to_excel(writer, 'REGR_DATA')

################## Prepare for second sheet
test_cat_count  = pd.DataFrame(columns=['TEST','COUNT'],index=range(1,1))
p               = pd.DataFrame(columns=['TEST','COUNT'],index=range(1,1))

for i in range(len(low_end)):
    #print (cat[i])
    #PASS cases
    
    if(low_end[i] == 123456789 or low_end[i] == 987654321 or low_end[i] == 135792468 or low_end[i] == 246813579):
        if(high_end[i] == 123456789):
            p = (regr_sorted[(regr_sorted.FAILURES == 123456789)]['TEST'].value_counts())
        if(high_end[i] == 987654321):
            p = (regr_sorted[(regr_sorted.FAILURES == 987654321)]['TEST'].value_counts())
        if(high_end[i] == 135792468):
            p = (regr_sorted[(regr_sorted.FAILURES == 135792468)]['TEST'].value_counts())
        if(high_end[i] == 246813579):
            p = (regr_sorted[(regr_sorted.FAILURES == 246813579)]['TEST'].value_counts())
            
        q = p.to_frame()
        q.reset_index(inplace=True)
        q.columns = ['TEST','COUNT']
        q['NO_OF_ERRORS'] = cat[i]
        #q['TYPE'] = test_type_final;
        test_cat_count = pd.concat([test_cat_count,q],ignore_index=True)
    else:
        if(low_end[i] == 0 and high_end[i] == 0):
            p = (regr_sorted[(regr_sorted.FAILURES == 0)]['TEST'].value_counts())
            q = p.to_frame()
            q.reset_index(inplace=True)
            q.columns = ['TEST','COUNT']
            q['NO_OF_ERRORS'] = cat[i]
            #q['TYPE'] = test_type_final;
            test_cat_count = pd.concat([test_cat_count,q],ignore_index=True)
        else:
            #ONLY one error cases
            if(low_end[i] == 1 and high_end[i] == 1):
                p = (regr_sorted[(regr_sorted.FAILURES == 1)]['TEST'].value_counts())
                q = p.to_frame()
                q.reset_index(inplace=True)
                q.columns = ['TEST','COUNT']
                q['NO_OF_ERRORS'] = cat[i]
                #q['TYPE'] = test_type_final;
                test_cat_count = pd.concat([test_cat_count,q],ignore_index=True)
                #print(test_cat_count)            
            else:
               p = (regr_sorted[(regr_sorted.FAILURES >= low_end[i]) & (regr_sorted.FAILURES <= high_end[i])]['TEST'].value_counts())
               q = p.to_frame()
               q.reset_index(inplace=True)
               q.columns = ['TEST','COUNT']
               q['NO_OF_ERRORS'] = cat[i]
               #q['TYPE'] = test_type_final;
               test_cat_count = pd.concat([test_cat_count,q],ignore_index=True)
            
            
#change order of columns
test_cat_count = test_cat_count[['TEST','NO_OF_ERRORS', 'COUNT']]

#print (test_cat_count)
#sys.exit()

#Extract SEED information
for i,row in test_cat_count.iterrows():
    #print(row['TEST']," ",row['NO_OF_ERRORS'], " ",row['COUNT'])
    #print("I: ",i," ",regr_sorted[(regr_sorted['TEST'] == row['TEST']) & (regr_sorted['STATUS'] == row['NO_OF_ERRORS'])]['SEED'])
    t1 = (regr_sorted[(regr_sorted['TEST'] == row['TEST']) & (regr_sorted['STATUS'] == row['NO_OF_ERRORS'])]['SEED'])
    t2 = list(t1)
    #print ("J: ",i," LIST: ",t2[0:2])
    test_cat_count.at[i,'SEED'] = t2[0]


#writer = pd.ExcelWriter('output.xlsx')
test_cat_count.to_excel(writer, 'ERROR_CAT_VIEW_1')


################ Preparing for third sheet
#https://seaborn.pydata.org/generated/seaborn.heatmap.html
#https://likegeeks.com/seaborn-heatmap-tutorial/
#https://heartbeat.fritz.ai/seaborn-heatmaps-13-ways-to-customize-correlation-matrix-visualizations-f1c49c816f07

#Changing formats using pivot tables
test_error_type = test_cat_count.drop(columns="SEED").pivot(index="TEST",columns="NO_OF_ERRORS")

#categorize tests
for i,row in test_error_type.iterrows():
    test_type = []
    test_type_code =[]
    type_flag = 0
    if('tile' in i):
        test_type.append('TILE')
        test_type_code.append('5')
        type_flag = 5
    if('db' in i):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('DB')
        test_type_code.append('1')
        type_flag = 1
    if('cdef' in i):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('CDEF')
        test_type_code.append('2')
        type_flag = 2
    if('lr' in i):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('LR')
        test_type_code.append('3')
        type_flag = 3
    if('upscale' in i):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('UPSCALE')
        test_type_code.append('4')
        type_flag = 4
    if('padded' in i):
        if(type_flag != 0):
            test_type.append('_')
        test_type.append('PADDED')
        test_type_code.append('6')
        type_flag = 6
    
    test_type_final = ''.join(test_type)
    test_type_code_final = ''.join(test_type_code)
    test_error_type.at[i,('COUNT','TEST_TYPE')] = test_type_final
    test_error_type.at[i,('COUNT','TEST_TYPE_CODE')] = test_type_code_final
    test_error_type.at[i,('COUNT','TOTAL')] = ''
    test_error_type.at[i,('COUNT','PASSED')] = ''

#change order of columns
column_names = [('COUNT','TEST_TYPE'),('COUNT','TEST_TYPE_CODE'),('COUNT','TOTAL'),('COUNT','PASSED')]
if(('COUNT','PASS') in test_error_type.columns):
    column_names.append(('COUNT','PASS'))
if(('COUNT','ONE_ERROR') in test_error_type.columns):
    column_names.append(('COUNT','ONE_ERROR'))
if(('COUNT','2_TO_10_ERRORS') in test_error_type.columns):
    column_names.append(('COUNT','2_TO_10_ERRORS'))
if(('COUNT','11_TO_50_ERRORS') in test_error_type.columns):
    column_names.append(('COUNT','11_TO_50_ERRORS'))
if(('COUNT', '51_TO_100_ERRORS') in test_error_type.columns):
    column_names.append(('COUNT', '51_TO_100_ERRORS'))
if(('COUNT','RAND_ERR') in test_error_type.columns):
    column_names.append(('COUNT','RAND_ERR'))
if(('COUNT','CSIM_CRASH') in test_error_type.columns):
    column_names.append(('COUNT','CSIM_CRASH'))
if(('COUNT','TIMEOUT') in test_error_type.columns):
    column_names.append(('COUNT','TIMEOUT'))


test_error_type = test_error_type[column_names]
test_error_type = test_error_type.sort_values(by=('COUNT','TEST_TYPE_CODE'))

test_type_init = 'TEMP'
test_error_type = test_error_type.fillna(0)
for i,row in test_error_type.iterrows():
    #print("I: ",i)
    #print("R: ",row)
    if(row[('COUNT','TEST_TYPE')] != test_type_init):
        test_type_init = row[('COUNT','TEST_TYPE')]
        total_pass_by_cat = 0
        total_by_cat = 0
    total_pass_by_cat = total_pass_by_cat + row[('COUNT','PASS')]
    test_error_type.at[i,('COUNT','PASSED')] = total_pass_by_cat

    test_error_type_col_names = list(test_error_type.columns)
    test_error_type_col_names = test_error_type_col_names[4:] 
    s = 0    
    for j in test_error_type_col_names:
        s = s + row[j]
        #print("ROW_J: ",row[j]," SUM: ",s)
    test_error_type.at[i,('COUNT','TOTAL')] = s

#	COUNT									
#NO_OF_ERRORS	TEST_TYPE	TEST_TYPE_CODE	PASS	ONE_ERROR	2_TO_10_ERRORS	11_TO_50_ERRORS	51_TO_100_ERRORS	RAND_ERR	CSIM_CRASH	TIMEOUT
#TEST										
#test_error_type = test_error_type.drop([0,2],axis=0)
test_error_type.to_excel(writer, 'ERROR_CAT_VIEW_2')

#Cell merging
#ws = writer.sheets['ERROR_CAT_VIEW_2']
#ws.merge_range('B4:B5', 'LR_MERGED')
#ws.save()


################### Prepare for fourth sheet
test_errors_with_seed = pd.pivot_table(test_cat_count,index=["TEST","NO_OF_ERRORS"],values=["COUNT","SEED"],aggfunc='first')
test_errors_with_seed.to_excel(writer, 'ERROR_CAT_VIEW_3')



pd1 =  (pd.pivot_table(regr_sorted,index=["TEST_TYPE"],values=["FAILURES"],aggfunc='count'))
pd2 =  (pd.pivot_table(regr_sorted,index=["TEST_TYPE","STATUS"],values=["FAILURES"],aggfunc='count'))
pd3 =  (pd.pivot_table(test_error_type,index=[("COUNT","TEST_TYPE")],values=[("COUNT","TOTAL")],aggfunc='sum'))
pd4 =  (pd.pivot_table(test_error_type,index=[("COUNT","TEST_TYPE")],values=[("COUNT","PASS")],aggfunc='sum'))

pd2.to_excel(writer, 'ERROR_CAT_VIEW_4')

status = pd.concat([pd3, pd4], axis=1)
status.columns = ['TOTAL','PASS']
status.insert(2,"%PASS",(status["PASS"]/status["TOTAL"])*100,True)
status.loc['TOTAL'] = [status['TOTAL'].sum(),status['PASS'].sum(),(status['PASS'].sum()/status['TOTAL'].sum()*100)]
status.to_excel(writer, 'STATUS_SUMMARY')

writer.save()

sys.exit()


################################ Below code is not used
plt.figure(figsize=(300,300))

heatmap_data = pd.pivot_table(test_cat_count, values='COUNT', 
                     index=['TEST'], 
                     columns='NO_OF_ERRORS',aggfunc='first')

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 100)

heatmap_data.to_excel('failure_data.xlsx', index=False)

sns.set(font_scale=8)
svm = sns.heatmap(heatmap_data, cmap="RdYlGn",annot=True,square=True,fmt='g')



sys.exit()

##[[1]] -- Extract tests with [X;Y] number of failures 
count_to_check = 20
#print(regr_sorted[(regr_sorted.FAILURES > 0) & (regr_sorted.FAILURES < count_to_check)])
print(regr_sorted[(regr_sorted.FAILURES > 0) & (regr_sorted.FAILURES < count_to_check)].count())

#print(regr_sorted[regr_sorted.index < 10])

##[[2]] -- Extact all PASSed tests
#print(regr_sorted[regr_sorted.FAILURES == 0])
print(regr_sorted[regr_sorted.FAILURES == 0].count())

##[[3]] -- Exctract number of tests PASSED per type of test
print("Number of tests PASSED per type of test")
p = regr_sorted[regr_sorted.FAILURES == 0]
p.columns = ['TEST','FAILURES']
#print(p)
print(p['TEST'].value_counts())