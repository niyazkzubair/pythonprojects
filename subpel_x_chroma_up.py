# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 08:09:18 2020

@author: nzubair
"""
SUPERRES_SCALE_BITS = 14;      
SUPERRES_EXTRA_BITS = 8;      
SUPERRES_SCALE_MASK = (1 << 14) - 1;      
	 
#For chroma   
up_scl_pic_width = 330
frame_width = 264

up_scl_pic_width_chroma = (up_scl_pic_width + 1) >> 1;
frame_width_chroma = (frame_width + 1) >> 1;
	 
step_x_chroma = ((frame_width_chroma << SUPERRES_SCALE_BITS) + (up_scl_pic_width_chroma/ 2)) / up_scl_pic_width_chroma;
err_chroma = (up_scl_pic_width_chroma * step_x_chroma) - (frame_width_chroma << SUPERRES_SCALE_BITS);

temp_1 = hex(up_scl_pic_width_chroma);
temp_2 = hex(frame_width_chroma);
	 
	 
temp_3 = (-((temp_1 - temp_2) << (SUPERRES_SCALE_BITS - 1)) + hex(up_scl_pic_width / 2));
temp_4 = hex(temp_3) / hex(temp_1);      
temp_5 = int(temp_3) / (temp_1) + ((1 << (SUPERRES_EXTRA_BITS - 1))) - (err_chroma / 2);
int_subpel_x_chroma = int(temp_5) & SUPERRES_SCALE_MASK;

 
print("NZUBAIR_UPSCALE_DEBUG -- HEX -- temp_1:%x temp_2:%x temp_3:%x temp_4:%x temp_5:%x int_subpel_x_chroma:%x",temp_1,temp_2,hex(int(temp_3)),hex(int(temp_4)),hex(int(temp_5)),int_subpel_x_chroma);
print("NZUBAIR_UPSCALE_DEBUG -- DEC -- temp_1:%d temp_2:%d temp_3:%d temp_4:%d temp_5:%d int_subpel_x_chroma:%d",temp_1,temp_2,temp_3,temp_4,temp_5,int_subpel_x_chroma);


print ("int_subpel_x_chroma :",int_subpel_x_chroma)