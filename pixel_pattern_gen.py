# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:06:24 2020

@author: nzubair
"""


import numpy as np
import matplotlib.pyplot as plt
import random

my_defines = {
    '8_BIT'     : 0,
    '10_BIT'    : 1,
    'PAT_0'     : 0,
    'PAT_1'     : 1,
    'PAT_2'     : 2,
    'PAT_3'     : 3,
    'PAT_4'     : 4,
    'PAT_5'     : 5,
    'PAT_6'     : 6,
    'PAT_7'     : 7,
    'PAT_8'     : 8,
    'PAT_9'     : 9,
    'PAT_10'     : 10,
    'PAT_11'     : 11,
    'PAT_12'     : 12,
    'PAT_13'     : 13,
    'PAT_14'     : 14,
    'PAT_15'     : 15,
    'PAT_16'     : 16,
    'PAT_17'     : 17,
    'PAT_18'     : 18,
    'PAT_19'     : 19,
    'PAT_20'     : 20,
    'PAT_21'     : 21,
    'PAT_22'     : 22
}

EIGHT_BIT = my_defines['8_BIT']
TEN_BIT   = my_defines['10_BIT']
PATTERN_0 = my_defines['PAT_0']
PATTERN_1 = my_defines['PAT_1']
PATTERN_2 = my_defines['PAT_2']
PATTERN_3 = my_defines['PAT_3']
PATTERN_4 = my_defines['PAT_4']
PATTERN_5 = my_defines['PAT_5']
PATTERN_6 = my_defines['PAT_6']
PATTERN_7 = my_defines['PAT_7']
PATTERN_8 = my_defines['PAT_8']
PATTERN_9 = my_defines['PAT_9']
PATTERN_10 = my_defines['PAT_10']
PATTERN_11 = my_defines['PAT_11']
PATTERN_12 = my_defines['PAT_12']
PATTERN_13 = my_defines['PAT_13']
PATTERN_14 = my_defines['PAT_14']
PATTERN_15 = my_defines['PAT_15']
PATTERN_16 = my_defines['PAT_16']
PATTERN_17 = my_defines['PAT_17']
PATTERN_18 = my_defines['PAT_18']
PATTERN_19 = my_defines['PAT_19']
PATTERN_20 = my_defines['PAT_20']
PATTERN_21 = my_defines['PAT_21']
PATTERN_22 = my_defines['PAT_22']

def ppg(fw, fh, bit_depth=0, gen_type=0, bw=10, bh=10, p1=0, p2=0):
    ppg_minor(fw, fh, bit_depth, gen_type, bw, bh, p1, p2)

def ppg_minor(fw, fh, bit_depth=0, gen_type=0, bw=10, bh=10, p1=0, p2=0):
    if(gen_type == 0):
        if(bit_depth == 0):
            frame_2 = np.random.randint(low=0, high=255, size=(fw,fh))
        else:
            frame_2 = np.random.randint(low=0, high=1023, size=(fw,fh))
    
    if(bit_depth == 0):
        pixel_max_value = 255;
        #pixel_max_value = int(np.random.randint(0,128, size=(1,1)))
    else:
        pixel_max_value = 1023;
    
    #horizontal bands
    if(gen_type == 1):
        frame_2 = np.zeros((fh,fw))
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                temp = int(i/bh)
                frame_2[i][j] = temp & pixel_max_value;
                
    #vertical bands
    if(gen_type == 2):
        frame_2 = np.zeros((fh,fw))
        for j in range(0,fw,1):
            for i in range(0,fh,1):
                temp = int(j/bw)
                #temp = int(j/random.randrange(1, 20, 1))
                frame_2[i][j] = temp & pixel_max_value;
    
    #horizontal strips
    if(gen_type == 3):
        frame_2 = np.zeros((fh,fw))
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                temp = int(((pixel_max_value + 1)/(fh/bh))*i)
                frame_2[i][j] = temp & pixel_max_value;
                
    #vertical strips
    if(gen_type == 4):
        frame_2 = np.zeros((fh,fw))
        for j in range(0,fw,1):
            for i in range(0,fh,1):
                temp = int(((pixel_max_value + 1)/(fw/bw))*j)
                frame_2[i][j] = temp & pixel_max_value;
                
    #checkers_1
    if(gen_type == 5):
        frame_2 = np.zeros((fh,fw))
        for j in range(0,fw,1):
            for i in range(0,fh,1):
                #temp = int(((pixel_max_value + 1)/(fw/bw))*j) + int(((pixel_max_value + 1)/(fh/bh))*i)
                temp = int(((pixel_max_value + 1)/(fw/bw))*j) + int(((pixel_max_value + 1)/(fh/bh))*i)
                frame_2[i][j] = temp & pixel_max_value;
        
        temp = int(np.random.randint(1,32, size=(1,1)))
        print("Factor: ",temp)
        for j in range(0,fw,1):
            for i in range(0,fh,1):
                if(j+temp<64):
                    frame_2[i][j] = frame_2[i][j+temp]
                
    #checkers_2
    if(gen_type == 6):
        frame_2 = np.zeros((fh,fw))
        r1 = int(np.random.randint(1,10, size=(1,1)))
        r2 = int(np.random.randint(1,10, size=(1,1)))
        for j in range(0,fw,1):
            for i in range(0,fh,1):
                temp_1 = int(((pixel_max_value + 1)/(fw/bw))*j)
                temp_2 = int(((pixel_max_value + 1)/(fh/bh))*i)
                temp = r1*temp_1 + r2*temp_2
                frame_2[i][j] = temp & pixel_max_value;
        print (r1, " ",r2)
        
    #grains
    if(gen_type == 7):
        frame_2 = np.zeros((fh,fw))
        for j in range(0,fw,1):
            for i in range(0,fh,1):
                temp_1 = int(((pixel_max_value + 1)/(fw/bw))*j)
                temp_2 = int(((pixel_max_value + 1)/(fh/bh))*i)
                r1 = int(np.random.randint(1,5, size=(1,1)))
                r2 = int(np.random.randint(1,5, size=(1,1)))
                temp = r1*temp_1 + r2*temp_2
                frame_2[i][j] = temp & pixel_max_value;
                
    if(gen_type == 8):
        frame_2 = np.zeros((fh,fw))
        r1 = int(np.random.randint(1,10, size=(1,1)))
        r2 = int(np.random.randint(1,10, size=(1,1)))
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                temp = int((pixel_max_value + 1)*(np.sin(r1*i*r2*j)))
                frame_2[i][j] = temp & pixel_max_value;
                
    if(gen_type == 9):
        frame_2 = np.zeros((fh,fw))
        r1 = int(np.random.randint(1,10, size=(1,1)))
        r2 = int(np.random.randint(1,10, size=(1,1)))
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                temp = int((pixel_max_value + 1)*(np.sin(r1*i + r2*j)))
                frame_2[i][j] = temp & pixel_max_value;
                
    if(gen_type == 10):
        frame_2 = np.zeros((fh,fw))
        r1 = int(np.random.randint(1,10, size=(1,1)))
        r2 = int(np.random.randint(1,10, size=(1,1)))
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                temp = int((pixel_max_value + 1)*(np.cos(r1*i*r2*j)))
                frame_2[i][j] = temp & pixel_max_value;
                
    if(gen_type == 11):
        frame_2 = np.zeros((fh,fw))
        r1 = int(np.random.randint(1,10, size=(1,1)))
        r2 = int(np.random.randint(1,10, size=(1,1)))
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                temp = int((pixel_max_value + 1)*(np.cos(r1*i + r2*j)))
                frame_2[i][j] = temp & pixel_max_value;
                
    #sin/cos/tan add/mult
    if(gen_type == 12):
        frame_2 = np.zeros((fh,fw))
        l1 = int(np.random.randint(0,1, size=(1,1)))
        l2 = int(np.random.randint(0,1, size=(1,1)))
        tool = int(np.random.randint(0,5, size=(1,1)))
        
        r1 = int(np.random.randint(1,10, size=(1,1)))
        r2 = int(np.random.randint(1,10, size=(1,1)))
        d1 = int(np.random.randint(1,10, size=(1,1)))
        d2 = int(np.random.randint(1,10, size=(1,1)))
        for i in range(0,fh,1):
            if(l1 == 1 and l2 == 0):
                r1 = int(np.random.randint(1,10, size=(1,1)))
                r2 = int(np.random.randint(1,10, size=(1,1)))
            for j in range(0,fw,1):
                if(l2):
                    r1 = int(np.random.randint(1,10, size=(1,1)))
                    r2 = int(np.random.randint(1,10, size=(1,1)))
                if(tool == 0):
                    temp = int((pixel_max_value + 1)*(np.sin(r1*i/d1*r2*j/d2)))
                if(tool == 1):
                    temp = int((pixel_max_value + 1)*(np.sin(r1*i/d1+r2*j/d2)))
                if(tool == 2):
                    temp = int((pixel_max_value + 1)*(np.cos(r1*i/d1*r2*j/d2)))
                if(tool == 3):
                    temp = int((pixel_max_value + 1)*(np.cos(r1*i/d1+r2*j/d2)))
                if(tool == 4):
                    temp = int((pixel_max_value + 1)*(np.tan(r1*i/d1*r2*j/d2)))
                if(tool == 0):
                    temp = int((pixel_max_value + 1)*(np.tan(r1*i/d1+r2*j/d2)))
                    
                frame_2[i][j] = temp & pixel_max_value;
           
    #diagonal linear intensity gradient
    if(gen_type == 13):
        frame_2 = np.zeros((fh,fw))
        r1 = int(np.random.randint(1,20, size=(1,1)))
        r2 = int(np.random.randint(1,4, size=(1,1)))
        tool = int(np.random.randint(0,7, size=(1,1)))
        
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                if(tool == 0):
                    temp = int((1-np.cos((i+j)*np.pi/min(fw,fh))/2))
                if(tool == 1):
                    temp = int((1-np.cos((i+j)*np.pi/r1)/2))
                if(tool == 2):
                    temp = int((1-np.cos((i*j)*np.pi/r1)/2))
                if(tool == 3):
                    temp = int((1-np.cos((i*j/r2)*np.pi/r1)/2))
                if(tool == 4):
                    temp = int((1-np.sin((i+j)*np.pi/min(fw,fh))/2))
                if(tool == 5):
                    temp = int((1-np.sin((i+j)*np.pi/r1)/2))
                if(tool == 6):
                    temp = int((1-np.sin((i*j)*np.pi/r1)/2))
                if(tool == 7):
                    temp = int((1-np.sin((i*j/r2)*np.pi/r1)/2))
                
                frame_2[i][j] = temp & pixel_max_value;
    
    #sine squared grey scale radial combinations
    if(gen_type == 14):
        frame_2 = np.zeros((fh,fw))
        tool = int(np.random.randint(0,2, size=(1,1)))
        r1_r2 = int(np.random.randint(0,2, size=(1,1)))    
        
        
        if(r1_r2 == 0):
            r1 = int(np.random.randint(1,50, size=(1,1)))
            r2 = int(np.random.randint(1,50, size=(1,1)))
        if(r1_r2 == 1):
            r1 = int(np.random.randint(1,5, size=(1,1)))
            r2 = int(np.random.randint(1,5, size=(1,1)))
        if(r1_r2 == 2):
            r1 = random.choice([10,20,30,40,50])
            r2 = random.choice([60,70,80,90,100])
        
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                if(tool == 0 or tool == 1):
                    temp = int((pixel_max_value + 1)* ((1-(np.cos(2*np.pi*np.sqrt(np.square(i/r1) + np.square(j/r2)))))/2))
                if(tool == 2):
                    temp = int((pixel_max_value + 1)* ((1-(np.cos(2*np.pi*np.sqrt(np.square(i*r1) + np.square(j*r2)))))/2))
                frame_2[i][j] = temp & pixel_max_value;
    
    if(gen_type == 15):
        frame_2 = np.zeros((fh,fw))
        tool = int(np.random.randint(0,2, size=(1,1)))
        r1_r2 = int(np.random.randint(0,2, size=(1,1)))  
        pix_add = int(np.random.randint(0,((pixel_max_value+1)/2), size=(1,1)))  
        
        if(r1_r2 == 0):
            r1 = int(np.random.randint(1,50, size=(1,1)))
            r2 = int(np.random.randint(1,50, size=(1,1)))
        if(r1_r2 == 1):
            r1 = int(np.random.randint(1,5, size=(1,1)))
            r2 = int(np.random.randint(1,5, size=(1,1)))
        if(r1_r2 == 2):
            r1 = random.choice([10,20,30,40,50])
            r2 = random.choice([60,70,80,90,100])
        
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                if(tool == 0):
                    temp = int(np.sqrt(np.square(i*r1) + np.square(j*r2)))
                if(tool == 1):
                    temp = int(pix_add + np.sqrt(np.square(i*r1) + np.square(j*r2)))
                if(tool == 2):
                    temp = int(np.square(i)*i*r1 + np.square(j)*j*r2)
                frame_2[i][j] = temp & pixel_max_value;  
        
        
    if(gen_type == 16):
        frame_2 = np.zeros((fh,fw))
        bit_list = []
        rand_list = random.sample(range(65536), int((fw*fh/4/4)))
        #print (rand_list)
        for i in rand_list:
            bin_i = bin(i)
            print ("I :",bin(i), " Length: ",len(bin_i))
            for j in range(len(bin_i),18): 
                bit_list.append(0)
            for j in range(2,len(bin_i)): 
                temp = bin_i[j]
                #print (temp)
                bit_list.append(temp)
        print(bit_list)
        l1 = []
        for i in bit_list:
            l1.append(int(i)*255)
        print (l1)     
        
        np_l1 = np.array(l1)
        np_l2 = np_l1.reshape(int(fw),int(fh))
        
        print (np_l2)
        
        for l in range(int(8/4)):
            print ("", end ="\n")
            for k in range(int(8/4)):
                print ("", end ="\n")
                for j in range(4):
                    print ("", end ="\n")
                    for i in range(4):
                        print ("(",i+4*k,",",j+4*l,")", end =" ")
                        print(np_l2[j+4*l][i+4*k], end =" ")
        frame_2 = np_l2
        
    if(gen_type == 17):
        frame_2 = np.zeros((fh,fw))
        r1 = int(np.random.randint(1,16*(1+3*bit_depth), size=(1,1)))
        r2 = int(np.random.randint(1,16*(1+3*bit_depth), size=(1,1)))
        print ("r1: ",r1," r2: ",r2)
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                frame_2[i][j] = int(np.random.randint(0,r1*r2, size=(1,1)));

                
    if(gen_type == 18):
        print("Here")
        frame_2 = np.zeros((fh,fw))
        flag = 0;
        for i in range(0,fh,1):
            for j in range(0,fw,1):
                if((i==0 and j==0) or (i%8==0 and j%8==0)):
                    flag = 1;
                    count = 0;
                    spots_in_8x8 = int(np.random.randint(0,64, size=(1,1)))
                    row_pos_frm_top = int(np.random.randint(1,5, size=(1,1)))
                    #print (i," ",j," ",spots_in_8x8," ",row_pos_frm_top)
                if(flag == 1 and j%row_pos_frm_top and count < spots_in_8x8):
                    count = count + 1
                    frame_2[i][j] = pixel_max_value;
                '''    
                if(flag == 1 and i%row_pos_frm_top and count < spots_in_8x8):
                    count = count + 1
                    frame_2[i][j] = pixel_max_value;
                    #print (i," ",j," ","---------------")
                '''
                if(count == spots_in_8x8):
                    flag = 0
                    
    if(gen_type == 19):
        if(bit_depth == 0):
            frame_2 = np.random.choice([0,127,255],size=(fw,fh))
        else:
            frame_2 = np.random.choice([0,127,255,512,1023],size=(fw,fh))
      
    if(gen_type == 20):
        frame_2 = np.zeros((fh,fw))
        max_val = 16
        r1 = int(np.random.randint(-max_val,max_val, size=(1,1)))
        
        pqr = int(fh/16)
        for k in range(pqr):
            for l in range(pqr):
                r2 = int(np.random.randint(0,max_val-1, size=(1,1)))
                pat_type = int(np.random.randint(0,8, size=(1,1)))
                #pat_type = 7
                
                print("pat_type: ",pat_type)
                for i in range(0,16,1):
                    for j in range(0,16,1):
                        
                        if((pat_type == 0 and j==i+r1) or
                           (pat_type == 1 and ((j==i+r1) or (j==i+r1+1))) or
                           (pat_type == 2 and (j==max_val-i+r1)) or
                           (pat_type == 3 and ((j==max_val-i+r1) or (j==max_val-i+r1+1))) or
                           (pat_type == 4 and (j==r2)) or 
                           (pat_type == 5 and (i==r2)) or
                           (pat_type == 6 and ((j==i+r1) or (j==i+r1-1)))
                           ):
                                frame_2[16*k+i][16*l+j] = pixel_max_value
                                
                        if(pat_type == 7):
                            if(bit_depth == 0):
                                frame_2[16*k+i][16*l+j] = np.random.choice([0,0,0,255,255])
                            else:
                                frame_2[16*k+i][16*l+j] = np.random.choice([0,0,0,1023,1023])
    
    if(gen_type == 21):
        if(bit_depth == 0):
            frame_2 = np.random.choice([0,0,0,255,255],size=(fw,fh))
        else:
            frame_2 = np.random.choice([0,0,0,1023,1023],size=(fw,fh))
            
                
    '''                
    for l in range(8):
        for k in range(8):
            np_l2[k][l] = l
    '''    
    #if(gen_type == 14):  
    frame_2 = frame_2.astype(int)
    #print("\nGENERATED NP ARRAY")        
    print(np.transpose(frame_2))
    plt.imshow(np.transpose(frame_2),cmap="gray")
    plt.savefig('trail.png')
    np.savetxt('PIXEL_PATTERN.txt', frame_2, fmt="%x") 
    

pattern_type = int(np.random.randint(1,22, size=(1,1)))
#pattern_type = 20
fw = 1024;
fh = 1024;
bitdepth = int(np.random.randint(0,2, size=(1,1)))

print("Pattern :",pattern_type," bitdepth :",bitdepth)

if(pattern_type == PATTERN_0):
    ppg(fw,fh,bitdepth,PATTERN_0)
if(pattern_type == PATTERN_1):
    #pattern 1 -- horizontal band
    temp = int(np.random.randint(1,16, size=(1,1)))
    print("Factor: ",temp)
    ppg(fw,fh,bitdepth,PATTERN_1,15,temp)
if(pattern_type == PATTERN_2):
    #pattern 2 -- vertical band
    temp = int(np.random.randint(1,32, size=(1,1)))
    print("Factor: ",temp)
    ppg(fw,fh,bitdepth,PATTERN_2,temp,3)
if(pattern_type == PATTERN_3):    
    #pattern 3 -- horizontal strip
    temp = int(np.random.randint(1,100, size=(1,1)))
    print("Factor: ",temp)
    ppg(fw,fh,bitdepth,PATTERN_3,15,temp)
if(pattern_type == PATTERN_4):    
    #pattern 4 -- vertical strip
    temp = int(np.random.randint(1,100, size=(1,1)))
    print("Factor: ",temp)
    ppg(fw,fh,bitdepth,PATTERN_4,temp,50)
if(pattern_type == PATTERN_5):    
    #pattern 5 -- checker_1
    ppg(fw,fh,bitdepth,PATTERN_5,15,30)
if(pattern_type == PATTERN_6):    
    #pattern 6 -- checker_2
    ppg(fw,fh,bitdepth,PATTERN_6,5,4)
if(pattern_type == PATTERN_7):    
    #pattern 7 -- grains
    ppg(fw,fh,bitdepth,PATTERN_7,7,4)
if(pattern_type == PATTERN_8):    
    #pattern 8 -- sine mult
    ppg(fw,fh,bitdepth,PATTERN_8,7,4)
if(pattern_type == PATTERN_9):    
    #pattern 9 -- sine add
    ppg(fw,fh,bitdepth,PATTERN_9,7,4)
if(pattern_type == PATTERN_10):    
    #pattern 10 -- cos mult
    ppg(fw,fh,bitdepth,PATTERN_10,7,4)
if(pattern_type == PATTERN_11):    
    #pattern 11 -- cos add
    ppg(fw,fh,bitdepth,PATTERN_11,7,4)
if(pattern_type == PATTERN_12):    
    #pattern 12 -- sin/cos/tan add/mult
    ppg(fw,fh,bitdepth,PATTERN_12)
if(pattern_type == PATTERN_13):    
    #pattern 13 -- diagonal linear intensity gradient
    ppg(fw,fh,bitdepth,PATTERN_13)
if(pattern_type == PATTERN_14):    
    #pattern 14 -- diagonal linear intensity gradient
    ppg(fw,fh,bitdepth,PATTERN_14)
if(pattern_type == PATTERN_15):    
    #pattern 15 -- diagonal linear intensity gradient
    ppg(fw,fh,bitdepth,PATTERN_15)
if(pattern_type == PATTERN_16):    
    #pattern 16 -- 4x4 random pattern
    ppg(fw,fh,bitdepth,PATTERN_16)
if(pattern_type == PATTERN_17):    
    #pattern 17 -- 4x4 random pattern
    ppg(fw,fh,bitdepth,PATTERN_17)
if(pattern_type == PATTERN_18):    
    #pattern 18 -- 4x4 random pattern
    ppg(fw,fh,bitdepth,PATTERN_18)
if(pattern_type == PATTERN_19):    
    #pattern 19 -- 4x4 random pattern
    ppg(fw,fh,bitdepth,PATTERN_19)
if(pattern_type == PATTERN_20):    
    #pattern 19 -- 4x4 random pattern
    ppg(fw,fh,bitdepth,PATTERN_20)
if(pattern_type == PATTERN_21):    
    #pattern 19 -- 4x4 random pattern
    ppg(fw,fh,bitdepth,PATTERN_21)

    








