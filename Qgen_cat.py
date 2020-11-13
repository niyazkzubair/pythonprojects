# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:57:56 2020

@author: nzubair
"""

import sys
import pandas as pd
import xlwt
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns


qgen_regr = pd.read_csv(r'confshort_regr__13th_Oct__part_2.csv') 
qgen_master_param_list = pd.read_excel(r'fe_swi_params_for_Conf_Short_full__29th_Sep.xls') 
xls_path = "Conf_short_failure_cat__13th_Oct__part_2.xls"
'''
qgen_regr = pd.read_csv(r'conf_short_regression_status.csv') 
qgen_master_param_list = pd.read_excel(r'fe_swi_params_for_Conf_short_full.xls') 
xls_path = "conf_short_error_buckets__10th_Oct.xls"
'''


s1 = qgen_master_param_list['Vector']
workbook = xlwt.Workbook();                              
sheet_1=workbook.add_sheet('Error_Buckets');

sheet_1.write(0,0,"no");
sheet_1.write(0,1,"test_name_1");
sheet_1.write(0,2,"test_name_2");
sheet_1.write(0,3,"seed");
sheet_1.write(0,4,"Frame");	
sheet_1.write(0,5,"status");	
sheet_1.write(0,6,"error_type");	
sheet_1.write(0,7,"standard");
sheet_1.write(0,8,"pic_height");	
sheet_1.write(0,9,"pic_width");	
sheet_1.write(0,10,"pic_height_mod_8");	
sheet_1.write(0,11,"pic_width_mod_8");	
sheet_1.write(0,12,"apply_grain");	
sheet_1.write(0,13,"grain_seed");	
sheet_1.write(0,14,"lcu_size");
sheet_1.write(0,15,"db_ena");
sheet_1.write(0,16,"cdef_ena");	
sheet_1.write(0,17,"lr_ena");	
sheet_1.write(0,18,"ru_size");	
sheet_1.write(0,19,"lr_uv_shift");	
sheet_1.write(0,20,"upscaling_ena");	
sheet_1.write(0,21,"superres_denom");
sheet_1.write(0,22,"up_scl_pic_width");
sheet_1.write(0,23,"tiles_enabled");
sheet_1.write(0,24,"mono_chroma_ena");	
sheet_1.write(0,25,"chroma_format_idc");	
sheet_1.write(0,26,"bitdepth_luma_minus8");
sheet_1.write(0,27,"num_vpp_pipes_minus1");	
sheet_1.write(0,28,"frame_restoration_type_cr");	
sheet_1.write(0,29,"frame_restoration_type_cb");	
sheet_1.write(0,30,"frame_restoration_type_y");	

row_counter = 1;
count = 0;
for i,row_1 in qgen_regr.iterrows():        
    #if (row_1['STATUS'] == 'FAILED' and 'recon_wr' in row_1['DESCRIPTION'] ):
    #if (row_1['STATUS'] == 'FAILED' and 'lbuf_wr' in row_1['DESCRIPTION'] ):
    #if (row_1['STATUS'] == 'FAILED' ):
    if (row_1['STATUS'] == 'FAILED' or row_1['STATUS'] == 'TIMEOUT'):
    #if (row_1['STATUS'] == 'FAILED' or row_1['STATUS'] == 'TIMEOUT' or row_1['STATUS'] == 'PASSED'):
        count = count + 1;
        test_name = row_1['TEST_CASE_NAME']
        temp = test_name.split('_')
        
        
        temp_2 ="";
        seq = ("_",temp[-2],"_",temp[-2]);
        pat = temp_2.join(seq);
        test_name = test_name.replace(pat,"")
        
        frame_number = int(temp[-2],16)
        #print (test_name," :",frame_number)
        for j,row_2 in qgen_master_param_list.iterrows():
            #print(frame_number,row_2['Frame'])
            if(test_name in row_2['Vector'] and frame_number == row_2['Frame']):
                 print ("--",count,"--",test_name," pat:",pat," :",frame_number)
                 
                 desc = " "
                 err_type = " "
                 
                 if(row_1['STATUS'] != "PASSED"):
                     desc = row_1['DESCRIPTION'];
                     err_type = desc
                     if("recon_wr" in desc):
                         err_type = "RECON_WR";
                     
                 if(row_1['STATUS'] != "PASSED" and "lbuf_wr" in desc):
                     if("buf_id=0" in desc):
                         err_type = "LBUF_BUF_ID_0"
                     if("buf_id=1" in desc):
                         err_type = "LBUF_BUF_ID_1"
                     if("buf_id=2" in desc):
                         err_type = "LBUF_BUF_ID_2"
                     if("buf_id=3" in desc):
                         err_type = "LBUF_BUF_ID_3"
                     if("buf_id=4" in desc):
                         err_type = "LBUF_BUF_ID_4"
                     if("buf_id=5" in desc):
                         err_type = "LBUF_BUF_ID_5"
                     if("buf_id=6" in desc):
                         err_type = "LBUF_BUF_ID_6"
                     if("buf_id=7" in desc):
                         err_type = "LBUF_BUF_ID_7"
                     if("buf_id=8" in desc):
                         err_type = "LBUF_BUF_ID_8"
                     if("buf_id=9" in desc):
                         err_type = "LBUF_BUF_ID_9"
                     if("buf_id=10" in desc):
                         err_type = "LBUF_BUF_ID_10"
                     if("buf_id=11" in desc):
                         err_type = "LBUF_BUF_ID_11"
                     if("buf_id=12" in desc):
                         err_type = "LBUF_BUF_ID_12"
                     if("buf_id=13" in desc):
                         err_type = "LBUF_BUF_ID_13"
                     if("buf_id=14" in desc):
                         err_type = "LBUF_BUF_ID_14"
                     if("buf_id=15" in desc):
                         err_type = "LBUF_BUF_ID_15"
                     if("buf_id=16" in desc):
                         err_type = "LBUF_BUF_ID_16"
                     
                     
                 sheet_1.write(row_counter,0,row_counter);
                 sheet_1.write(row_counter,1,row_1['TEST_CASE_NAME']);
                 sheet_1.write(row_counter,2,row_2['Vector']);
                 sheet_1.write(row_counter,3,0);
                 sheet_1.write(row_counter,4,frame_number);	
                 sheet_1.write(row_counter,5,row_1['STATUS']);	
                 sheet_1.write(row_counter,6,err_type);	
                 sheet_1.write(row_counter,7,row_2['standard']);
                 sheet_1.write(row_counter,8,row_2['pic_height']);	
                 sheet_1.write(row_counter,9,row_2['pic_width']);	
                 sheet_1.write(row_counter,10,row_2['pic_height']%8);	
                 sheet_1.write(row_counter,11,row_2['pic_width']%8);	
                 sheet_1.write(row_counter,12,row_2['apply_grain']);	
                 sheet_1.write(row_counter,13,row_2['grain_seed']);	
                 sheet_1.write(row_counter,14,row_2['lcu_size']);
                 sheet_1.write(row_counter,15,row_2['db_ena']);
                 sheet_1.write(row_counter,16,row_2['cdef_ena']);	
                 sheet_1.write(row_counter,17,row_2['lr_ena']);	
                 sheet_1.write(row_counter,18,row_2['ru_size']);	
                 sheet_1.write(row_counter,19,row_2['lr_uv_shift']);	
                 sheet_1.write(row_counter,20,row_2['upscaling_ena']);	
                 sheet_1.write(row_counter,21,row_2['superres_denom']);
                 sheet_1.write(row_counter,22,row_2['up_scl_pic_width']);
                 sheet_1.write(row_counter,23,row_2['tiles_enabled']);
                 sheet_1.write(row_counter,24,row_2['mono_chroma_ena']);	
                 sheet_1.write(row_counter,25,row_2['chroma_format_idc']);	
                 sheet_1.write(row_counter,26,row_2['bitdepth_luma_minus8']);
                 sheet_1.write(row_counter,27,row_2['num_vpp_pipes_minus1']);	
                 sheet_1.write(row_counter,28,row_2['frame_restoration_type_cr']);	
                 sheet_1.write(row_counter,29,row_2['frame_restoration_type_cb']);	
                 sheet_1.write(row_counter,30,row_2['frame_restoration_type_y']);	
                 row_counter = row_counter + 1;
                 break


workbook.save(xls_path);

            