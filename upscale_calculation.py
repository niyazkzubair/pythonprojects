# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:22:09 2020

@author: nzubair
"""
import math

upscale_fw_list = []
step_x_luma_list = []
err_luma_list = []
int_subpel_x_luma_list = []
step_x_chroma_list = []
err_chroma_list = []
int_subpel_x_chroma_list = []

upscale_fw_unique_list = []
step_x_luma_unique_list = []
err_luma_unique_list = []
int_subpel_x_luma_unique_list = []
step_x_chroma_unique_list = []
err_chroma_unique_list = []
int_subpel_x_chroma_unique_list = []


def unique(list1): 
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
            
    # print list 
    for x in unique_list: 
        #print (x,) 
        upscale_fw_unique_list.append(x)
    
    print("Size of unique list: ",len(unique_list))
    unique_list.sort()
    print (unique_list)


SUPERRES_SCALE_BITS = 14;      
SUPERRES_EXTRA_BITS = 8;      
SUPERRES_SCALE_MASK = (1 << 14) - 1; 
  
for frame_width in range (16,17,1):
    for denom in range (9,17,1):
        upscale_fw = math.ceil((frame_width * denom -(denom/2))/8);
        upscale_fw = int((frame_width * denom -(denom/2))/8);
        #print ("FW: ",frame_width,"DENOM :",denom,"UPSCALE_FW: ",upscale_fw)
        upscale_fw_list.append(upscale_fw)
        
        up_scl_pic_width = upscale_fw
        
        #CALCx for LUMA
        step_x_luma = int(((frame_width << SUPERRES_SCALE_BITS) + (up_scl_pic_width/ 2)) / up_scl_pic_width);
        err_luma = (up_scl_pic_width * step_x_luma) - (frame_width << SUPERRES_SCALE_BITS);
        
        step_x_luma_list.append(step_x_luma)
        
        temp_1 = up_scl_pic_width;
        temp_2 = frame_width;
        temp_3 = (-((temp_1 - temp_2) << (SUPERRES_SCALE_BITS - 1)) + up_scl_pic_width / 2);
        temp_4 = int((temp_3) / (temp_1));      
        temp_5 = int((temp_3) / (temp_1) + ((1 << (SUPERRES_EXTRA_BITS - 1))) - (err_luma / 2));
        int_subpel_x_luma = int(temp_5) & SUPERRES_SCALE_MASK;
        
        int_subpel_x_luma_list.append(int_subpel_x_luma)
     
        
        
        up_scl_pic_width_chroma = (up_scl_pic_width + 1) >> 1;
        frame_width_chroma = (frame_width + 1) >> 1;
        
        step_x_chroma = ((frame_width_chroma << SUPERRES_SCALE_BITS) + (up_scl_pic_width_chroma/ 2)) / up_scl_pic_width_chroma;
        err_chroma = (up_scl_pic_width_chroma * step_x_chroma) - (frame_width_chroma << SUPERRES_SCALE_BITS);
        
        temp_1 = up_scl_pic_width_chroma;
        temp_2 = frame_width_chroma;
        temp_3 = (-((temp_1 - temp_2) << (SUPERRES_SCALE_BITS - 1)) + up_scl_pic_width / 2);
        temp_4 = (temp_3) / (temp_1);      
        temp_5 = int((temp_3) / (temp_1) + ((1 << (SUPERRES_EXTRA_BITS - 1))) - (err_chroma / 2));
        int_subpel_x_chroma = (temp_5) & SUPERRES_SCALE_MASK;

print ("(1) -- All possible values for upscale width :",len(upscale_fw_list))
print ("Unique values of upscale frame width")
unique(upscale_fw_list)

print ("(2) -- All possible values for step_x_luma :",len(step_x_luma_list))
print ("Unique values of step_x_luma")
unique(step_x_luma_list)

print ("(4) -- All possible values for int_subpel_x_luma_list :",len(int_subpel_x_luma_list))
print ("Unique values of int_subpel_x_luma_list")
unique(int_subpel_x_luma_list)
        
'''
       temp_1 = up_scl_pic_width;
       temp_2 = frame_width;


       temp_3 = (-((temp_1 - temp_2) << (SUPERRES_SCALE_BITS - 1)) + up_scl_pic_width / 2);
       temp_4 = $signed(temp_3) / $signed(temp_1);      
       temp_5 = $signed(temp_3) / $signed(temp_1) + $signed((1 << (SUPERRES_EXTRA_BITS - 1))) - $signed(err_luma / 2);
       int_subpel_x_luma = $signed(temp_5) & SUPERRES_SCALE_MASK;
       '''