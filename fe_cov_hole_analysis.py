# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 08:46:15 2020

@author: nzubair
"""

import pandas as pd
from tabulate import tabulate

cp_list = []
start_flag = 0
print_it = 0
count = 0
cp_found = 0
found_percentage = 0
print_only_uncovered = 1
cover_group_list = []
identified_cross = 0;

cov_df = pd.DataFrame(columns = ['COV_POINT','COV_PERCENTAGE','HIT_BINS','MISS_BINS','TOTAL_BINS'])
miss_df = pd.DataFrame(columns = ['CROSS','MISS_PATTERN','MISS_BINS'])

pd.options.display.max_columns = None
pd.options.display.width=None
detected_cov_group = 0;

tot_bb_tot_bins = 0;
tot_bb_hit_bins = 0;

tot_wb_tot_bins = 0;
tot_wb_hit_bins = 0;

for line in (open('report.txt')):
        #print ("LINE :",line)
        if('TYPE' in line and 'fg_av1d' not in line and 'fe_fg' not in line):
            #print (line)
            temp = line.split('/')
            cover_group_name = temp[-1]
            detected_cov_group = 1;
        if(detected_cov_group == 1 and 'covered/' in line):
            temp = line.split()
            hit = temp[2]
            total_bins = temp[3]
            temp = cover_group_name.split()
            
            if('_BB_' in temp[0]):    
                print (temp[0], "\t",total_bins,"\t",hit,"\t",int(total_bins)-int(hit))
                tot_bb_tot_bins = tot_bb_tot_bins + int(total_bins)
                tot_bb_hit_bins = tot_bb_hit_bins + int(hit)
            if('_WB_' in temp[0]):
                if('fe_av1d_WB_CDEF_Internal_Stall_cov' not in temp[0] and 
                   'fe_av1d_WB_LBUF_RD_buf_id_delay_cov' not in temp[0] and 
                   'fe_av1d_WB_LBUF_RD_buf_id_stall_cov' not in temp[0] and 
                   'fe_av1d_WB_LBUF_WR_buf_id_stall_cov' not in temp[0] and 
                   'fe_av1d_WB_Stall_on_LBUF_Buf_Ids_cov' not in temp[0]):
                    
                    if('fe_av1d_WB_CDEF_Final_filter_cov' in temp[0]):
                        #Some unexpected auto bins are present
                        total_bins = int(total_bins) - 108
                        '''
                    if('fe_av1d_WB_CDEF_Cost_cov' in temp[0]):
                        #Varstr >12 is not valid
                        total_bins = int(total_bins) - 96
                        '''
                        '''
                    if('fe_av1d_WB_ipif_rreq_cov' in temp[0]):
                        #when ibc_tile=valid, tile will be enabled
                        total_bins = int(total_bins) - 32 
                        '''
                        

                    
                    print (temp[0], "\t",total_bins,"\t",hit,"\t",int(total_bins)-int(hit))
                    tot_wb_tot_bins = tot_wb_tot_bins + int(total_bins)
                    tot_wb_hit_bins = tot_wb_hit_bins + int(hit)
            detected_cov_group = 0;
            '''
        if(detected_cov_group == 1 and 'missing/' in line):
            print (line)
            detected_cov_group = 0;
            '''
        if(cp_found == 1 and found_percentage == 0):
            line_split = line.split(' ')
            for i in line_split:
                if("%" in i):
                    percentage_cov = i
                    found_percentage = 1
                    cp_found = 0
                    break;
        if("TYPE" in line):
            start_flag = 0;
            
        #if("TYPE" in line and ("fe_av1d_cov_swi_csim_cov" in line)):
        if("TYPE" in line and ("se2fe" in line)):
        #if("TYPE" in line and ("fe_av1d_cov_swi_csim_cov" in line or "se2fe" in line)):
        #if("TYPE" in line):
            line_split = line.split(' ')
            for i in line_split:
                if("cov" in i):
                    if(i not in cover_group_list):
                        cover_group_list.append(i)
                    
                        if(start_flag == 0):
                            start_flag = 1;
                            count = count + 1
                            #print (line)
                        #else:
                        #start_flag = 0;
        
        if("Cross" in line):
            identified_cross = 0
        
        if(start_flag == 1 and print_it == 1 and "covered/total bins" in line):
            line_split = line.split(' ')
            for i in line_split:
                if(str(i).isnumeric()):
                    hit_bin_count = i
                    break;
                    
        if(start_flag == 1 and print_it == 1 and "missing/total bins:" in line):
            line_split = line.split(' ')
            for i in line_split:
                if(str(i).isnumeric()):
                    miss_bin_count = i
                    if(percentage_cov != "100.00%" or print_only_uncovered == 0):
                        #print(cp,"\t ",percentage_cov,"\tH:",hit_bin_count,"\tM:",miss_bin_count,"\tT:",int(hit_bin_count)+int(miss_bin_count))
                        
                        cov_df.loc[-1] = [cp,percentage_cov,int(hit_bin_count),int(miss_bin_count),int(hit_bin_count)+int(miss_bin_count)]
                        cov_df.index = cov_df.index + 1
            
                        print_it = 0
                        break;
                        
        if(identified_cross == 1 and "ZERO" in line and "ignore_bin" not in line):
            #print (cp)
            #print (line)
            line_split = line.split(' ')
            miss_pattern = '---'
            for i in line_split:
                if("<" in i):
                    miss_pattern = i
                if(str(i).isnumeric()):
                    missing_bins = int(i)
            #print (miss_pattern)
            #print (missing_bins)
            
            miss_df.loc[-1] = [cp,miss_pattern,int(missing_bins)]
            miss_df.index = miss_df.index + 1
            
                    
        #if(count == 1 and start_flag == 1 and ("Coverpoint" in line or "Cross " in line) and "swi" in line and "Uncovered" in line):
        if(start_flag == 1 and ("Coverpoint" in line or "Cross " in line)  and ("swi" in line or "Q2_pkt" in line)):
            identified_cross = 0;
            #print(line)
            #Coverpoint Q2_swi_upscale_frame_width              78.32%        100          -
            line_split = line.split(' ')
            #print(line_split)
            cp = line_split[5]
            cp_found = 1
            found_percentage = 0
            for i in line_split:
                if("%" in i):
                    percentage_cov = i
                    found_percentage = 1
                    break;
            if(cp not in cp_list):
                cp_list.append(cp)
                print_it = 1;
            #if("Cross" in line and "upsca" in line):
            if("Cross" in line):
                identified_cross = 1;

#### SHEET - 1: COV SUMMARY (HIT-MISS-TOTAL)
cov_df = cov_df.sort_values(by='MISS_BINS',ascending=False)
cov_df = cov_df.reset_index(drop=True)
writer = pd.ExcelWriter('fe_cov_holes.xls', engine='xlsxwriter')  
cov_df.to_excel(writer, 'HOLE_TABLE')
#print(tabulate(cov_df,headers='firstrow'))


#### SHEET - 2: COV SUMMARY OF UPSCALE CROSSES
cov_df_non_upscale = cov_df[cov_df["COV_POINT"].str.contains('upscal',case=False,regex=True)]
cov_df_non_upscale.to_excel(writer, 'HT_US')

workbook  = writer.book
worksheet = writer.sheets['HT_US']
format = workbook.add_format()
format.set_align('center')
format.set_align('vcenter')
worksheet.set_column('D:F',5, format)

#### SHEET - 3: COV SUMMARY OF NON-UPSCALE CROSSES
cov_df_upscale = cov_df[~cov_df["COV_POINT"].str.contains('upscal',regex=True)]
cov_df_upscale.to_excel(writer, 'HT_NON_US')


worksheet = writer.sheets['HT_NON_US']
fmt = workbook.add_format()
fmt.set_align('center')
fmt.set_align('vcenter')
worksheet.set_column('D:F',5, fmt)


#### SHEET - 4: CROSS COVERAGE HOLE SUMMARY
miss_df = miss_df.drop_duplicates() 
miss_df = miss_df.sort_values(by='MISS_BINS',ascending=False)
miss_df.to_excel(writer, 'HOLE_ANALYSIS')

#### SHEET - 5: CROSS COVERAGE HOLES WITHOUT UPSCALE parameter
miss_df_non_upscale = miss_df[~miss_df["CROSS"].str.contains('upscal',regex=True)]
miss_df_non_upscale.to_excel(writer, 'HOLE_ANALYSIS_NON_US')

writer.save()

tot_bb_tot_bins = 35709

print("-----------------------------------------------------------------")
print("Total_BB_bins: ",tot_bb_tot_bins)
print("Total_BB_hit: ",tot_bb_hit_bins)
print("Total_BB_holes: ",tot_bb_tot_bins - tot_bb_hit_bins)
print("BB % Coverage Hit: ",tot_bb_hit_bins/tot_bb_tot_bins*100)

print("-----------------------------------------------------------------")

print("Total_WB_bins: ",tot_wb_tot_bins)
print("Total_WB_hit: ",tot_wb_hit_bins)
print("Total_WB_holes: ",tot_wb_tot_bins - tot_wb_hit_bins)
print("WB % Coverage Hit: ",tot_wb_hit_bins/(tot_wb_tot_bins)*100)

print("-----------------------------------------------------------------")

print("80% --",tot_wb_tot_bins*.8," ",tot_wb_hit_bins - tot_wb_tot_bins*.8)
print("85% --",tot_wb_tot_bins*.85," ",tot_wb_hit_bins - tot_wb_tot_bins*.85)
print("87% --",tot_wb_tot_bins*.87," ",tot_wb_hit_bins - tot_wb_tot_bins*.87)
print("90% --",tot_wb_tot_bins*.9," ",tot_wb_hit_bins - tot_wb_tot_bins*.9)
print("92% --",tot_wb_tot_bins*.92," ",tot_wb_hit_bins - tot_wb_tot_bins*.92)
print("95% --",tot_wb_tot_bins*.95," ",tot_wb_hit_bins - tot_wb_tot_bins*.95)
print("96% --",tot_wb_tot_bins*.96," ",tot_wb_hit_bins - tot_wb_tot_bins*.96)
print("97% --",tot_wb_tot_bins*.97," ",tot_wb_hit_bins - tot_wb_tot_bins*.97)
print("98% --",tot_wb_tot_bins*.98," ",tot_wb_hit_bins - tot_wb_tot_bins*.98)

print("-----------------------------------------------------------------")




#print(tabulate(cov_df_non_upscale,headers='firstrow'))
