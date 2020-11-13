# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:42:04 2020

@author: nzubair
"""

# importing required modules 
import PyPDF2 
import re
import sys
import pandas as pd
import os


# Returns the longest repeating non-overlapping 
# substring in str 
#https://www.geeksforgeeks.org/longest-repeating-and-non-overlapping-substring/
def longestRepeatedSubstring(str): 
  
    n = len(str) 
    LCSRe = [[0 for x in range(n + 1)]  
                for y in range(n + 1)] 
  
    res = "" # To store result 
    res_length = 0 # To store length of result 
  
    # building table in bottom-up manner 
    index = 0
    for i in range(1, n + 1): 
        for j in range(i + 1, n + 1): 
              
            # (j-i) > LCSRe[i-1][j-1] to remove 
            # overlapping 
            if (str[i - 1] == str[j - 1] and
                LCSRe[i - 1][j - 1] < (j - i)): 
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
  
                # updating maximum length of the 
                # substring and updating the finishing 
                # index of the suffix 
                if (LCSRe[i][j] > res_length): 
                    res_length = LCSRe[i][j] 
                    index = max(i, index) 
                  
            else: 
                LCSRe[i][j] = 0
  
    # If we have non-empty result, then insert  
    # all characters from first character to  
    # last character of string 
    if (res_length > 0): 
        for i in range(index - res_length + 1, 
                                    index + 1): 
            res = res + str[i - 1] 
  
    return res 


#######################################################################################################
def read_one_pdf_file_and_extract_data(filename):
    # creating a pdf file object 
    #pdfFileObj = open('AC_STATEMENT_147201XXXX7645_25APR2020_01MAY2020_03052020141313.pdf', 'rb') 
    pdfFileObj = open(filename, 'rb') 
    
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    pdfReader.decrypt('HIRA1204')
     
    # printing number of pages in pdf file 
    print("Number of pages :", pdfReader.numPages) 
      
    # creating a page object 
    pageObj = pdfReader.getPage(0) 
      
    # extracting text from page 
    text = (pageObj.extractText())
    
    ##Raw input data read from pdf
    #print (text)
    
    temp = text.split('Statement of Account for the period')
    transaction_data = temp[1]
    
    split_transactions = transaction_data.split('CR')
    
    #Clean up data
    j = 0
    
    #print (split_transactions)
    for trans in split_transactions:
        
        i = trans
        
        if('/2020' in i):
            temp = trans.replace('/2020','/2020XYZ')
            temp = temp.split('XYZ')
        
            i = temp[1]+temp[2]
        
        #Remove below entries
        #CLG - Corresponds to cheque
        if('Opening Balance' in i or 'GRAND TOTAL' in i or 'CLG' in i or '' == i or 'SELF' in i):
            if('CLG' in i):
                print("Cheque transaction entry :",i)
            else:
                print("skip")
        else:
            #Starting of particulars
            i = i.replace('UPI IN',' UPIIN')
            i = i.replace('UPIIN',' UPIIN')
            i = i.replace('NFT',' NFT')
            i = i.replace('FN',' FN')
            
            #Type of transactions
            i = i.replace('CASH',' CASH ')
            i = i.replace('FT',' FT ')
            #i = i.replace('SBINT',' FT ')
            i = i.replace('TFR',' TFR ')
            i = i.replace('CLG',' CLG ')
            i = i.replace('MB',' MB ')
            
            #Correcting double fix
            i = i.replace('N FT ','NFT')
            i = i.replace('MB   FT B/ MB ','MB FTB/MB')
            i = i.replace('FT  IMPS','FT IMPS')
            
            i = i.replace('.00','.00XYZ')
            
            #Remove the entriesd from Dr/Cr column
            i_split = i.split("XYZ")
            temp = i_split[0]
            i = temp
            
            print ('-----------------------------------')
            print ("Raw Entry :",i)
            
            #Remove the repeated transaction code
            lrss = longestRepeatedSubstring(i)
            if('/' not in lrss and 'UPI' not in lrss and 'MB' not in lrss):
                #Below is the repeated transaction details, which need to be removed
                #print (lrss)
                #Repace the lrss with a PATTERN so that the second occurance can be removed
                
                i = i.replace(lrss,'XYZ',1)
                i = i.replace(lrss,'')
                i = i.replace('XYZ',lrss,1)
                
            
            #split to columns
            #UPIIN - TFR
            if(' UPIIN' in i):
                i = i.replace(' UPIIN',' UPIINASDF')
                i = i.replace(' TFR',' TFRZXCV')
                temp = (re.split('UPIIN|TFR',i))
                #print ("Intermediate_1: ",j,temp)
                if(len(temp) != 3):
                    print ("ERROR - [SPLIT_ERROR_1] -- Issue with splitting, expected 3, but list has more -- ",len(temp))
                
                for ijk in temp:
                    if ('ASDF' in ijk):
                        #print (ijk.replace('ASDF','UPIIN'))
                        transaction = (ijk.replace('ASDF','UPIIN'))
                    elif('ZXCV' in ijk):
                        #print (ijk.replace('ZXCV','TFR'))
                        ijk = (ijk.replace('ZXCV','TFR'))
                        ijk = ijk.split()
                        trans_type = ijk[0]
                        amount = ijk[1]
                    else:
                        #print (ijk)
                        date = ijk
            
            #FN - TFR
            elif(' FN' in i):
                i = i.replace(' FN',' FNASDF')
                i = i.replace(' TFR',' TFRZXCV')
                temp = (re.split('FN|TFR',i))
                #print ("Intermediate_2: ",j,temp)
                if(len(temp) != 3):
                    print ("ERROR - [SPLIT_ERROR_2] -- Issue with splitting, expected 3, but list has more -- ",len(temp))
                    sys.exit()
                
                for ijk in temp:
                    if ('ASDF' in ijk):
                        #print (ijk.replace('ASDF','FN'))
                        transaction = (ijk.replace('ASDF','FN'))
                    elif('ZXCV' in ijk):
                        #print (ijk.replace('ZXCV','TFR'))
                        ijk = (ijk.replace('ZXCV','TFR'))
                        ijk = ijk.split()
                        trans_type = ijk[0]
                        amount = ijk[1]
                    else:
                        #print (ijk)
                        date = ijk
            
            #FT IMPS - TFR
            elif(' FT IMPS' in i):
                i = i.replace(' FT IMPS',' FT IMPSASDF')
                i = i.replace(' TFR',' TFRZXCV')
                temp = (re.split('FT IMPS|TFR',i))
                #print ("Intermediate_3: ",j,temp)
                #if(len(temp) != 3):
                    #print ("ERROR - [SPLIT_ERROR_3] -- Issue with splitting, expected 3, but list has more -- ",len(temp))
                    #sys.exit()
                
                for ijk in temp:
                    if ('ASDF' in ijk):
                        #print (ijk.replace('ASDF','FT IMPS'))
                        transaction = (ijk.replace('ASDF','FT IMPS'))
                    elif('ZXCV' in ijk):
                        #print (ijk.replace('ZXCV','TFR'))
                        ijk = (ijk.replace('ZXCV','TFR'))
                        ijk = ijk.split()
                        trans_type = ijk[0]
                        amount = ijk[1]
                    else:
                        #print (ijk)
                        date = ijk
                        
            #NFT - FT
            elif(' NFT/' in i):
                i = i.replace(' NFT/',' NFETASDF/') #NFET is used instead of NFT to separate out NFT from FT
                i = i.replace(' FT',' FTZXCV')
                temp = (re.split('NFET|FT',i))
                #print ("Intermediate_4: ",j,temp)
                if(len(temp) != 3):
                    print ("ERROR - [SPLIT_ERROR_4] -- Issue with splitting, expected 3, but list has more -- ",len(temp))
                    sys.exit()
                
                for ijk in temp:
                    if ('ASDF' in ijk):
                        #print (ijk.replace('ASDF','NFT'))
                        transaction = (ijk.replace('ASDF','NFT'))
                    elif('ZXCV' in ijk):
                        #print (ijk.replace('ZXCV','FT'))
                        ijk = (ijk.replace('ZXCV','FT'))
                        ijk = ijk.split()
                        trans_type = ijk[0]
                        amount = ijk[1]
                    else:
                        #print (ijk)
                        date = ijk
                        
            #MB FTB - MB
            elif(' MB FTB' in i):
                i = i.replace('MB FTB','MIB FTBASDF') #MIB is used instead of MIB to separate out MB FTB from MB
                i = i.replace(' MB',' MJBZXCV')
                temp = (re.split('MIB FTB|MJB',i))
                #print ("Intermediate_5: ",j,temp)
                if(len(temp) != 3):
                    print ("ERROR - [SPLIT_ERROR_5] -- Issue with splitting, expected 3, but list has more -- ",len(temp))
                    sys.exit()
                
                for ijk in temp:
                    if ('ASDF' in ijk):
                        #print ("T :",ijk.replace('ASDF','MB FTB'))
                        transaction = ijk.replace('ASDF','MB FTB')
                    elif('ZXCV' in ijk):
                        #print ("A :",ijk.replace('ZXCV','MB'))
                        ijk = ijk.replace('ZXCV','MB')
                        ijk = ijk.split()
                        trans_type = ijk[0]
                        amount = ijk[1]
                    else:
                        #print ("D :",ijk)
                        date = ijk
        
            else :
                print ('Hai')
                #print ("ERROR - New type of transaction found -- in file: ",filename, "Entry :",i)
                #sys.exit()
            
            trans_entry.loc[-1] = [pd.to_datetime(date,dayfirst = True),transaction,trans_type,amount]
            trans_entry.index = trans_entry.index + 1
    
        j = j + 1;

    # closing the pdf file object 
    pdfFileObj.close() 

#Program start here
trans_entry = pd.DataFrame(columns = ['DATE','TRANSACTION DETAILS','TRANS_TYPE','AMOUNT'])
writer = pd.ExcelWriter('bank_transactions.xlsx') 

#Iterate over all pdf files

directory = r'C:\Anaconda\input'
for filename in os.listdir(directory):
    if ("AC_STATEMENT_" in filename and filename.endswith(".pdf")):
        print(os.path.join(directory, filename))
        file_path = (os.path.join(directory, filename))
        read_one_pdf_file_and_extract_data(file_path)
    else:
        continue
trans_entry = trans_entry.sort_values(by="DATE")
trans_entry['DATE'] = trans_entry['DATE'].dt.date
trans_entry.to_excel(writer)
writer.save()

