# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:32:32 2020

@author: nzubair
"""
#https://pyttsx3.readthedocs.io/en/latest/

# Python program to show 
# how to convert text to speech 
import pyttsx3 
  
# Initialize the converter 
converter = pyttsx3.init() 
  
# Set properties before adding 
# Things to say 
  
# Sets speed percent  
# Can be more than 100 
converter.setProperty('rate', 150) 
# Set volume 0-1 
converter.setProperty('volume', 1.0) 

volume = converter.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume) 
  
# Queue the entered text  
# There will be a pause between 
# each one like a pause in  
# a sentence 
converter.say("Python is Nice")
converter.say("")           
# Empties the say() queue 
# Program will not continue 
# until all speech is done talking 
converter.runAndWait() 