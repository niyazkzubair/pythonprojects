# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:28:09 2022

@author: nzubair
"""

#https://www.geeksforgeeks.org/python-boxlayout-widget-in-kivy/

# code to show how to use nested boxlayouts.
 
# import kivy module
import kivy
import prayer_times
from datetime import date


# this restricts the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")
   
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
   
# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button
 
# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the children at the desired location.
from kivy.uix.boxlayout import BoxLayout


import arabic_reshaper 
#conda install -c mpcabd arabic-reshaper

############ Weather ##############
# import required modules
import requests
 
# Enter your API key here
api_key = "67230857bba152d07e4572e7b889a0a3"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
#city_name = input("Enter city name : ")
#city_name = 'Calicut'
city_name = 'Poway'
 
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object
# convert json format data into
# python format data
x = response.json()
####################################



############## Stock ###############
#https://site.financialmodelingprep.com/developer/docs
stock_api_key = "1430f6577b2fb0931ae3a28368dcb3fc"
complete_url = "https://financialmodelingprep.com/api/v3/company/discounted-cash-flow/QCOM?apikey="+ stock_api_key
response = requests.get(complete_url)
stock = response.json()
#print (stock['Stock Price'])

############## Currency Exchange ########
#https://app.exchangerate-api.com/dashboard
currency_exchange_api_key = "f32a63a5337a50ab4130f0ae"
complete_url = "https://v6.exchangerate-api.com/v6/"+ currency_exchange_api_key + "/latest/USD"
response = requests.get(complete_url)
c_e = response.json()
#print (c_e["conversion_rates"]["INR"])

############## Quran ####################
complete_url = "http://api.alquran.cloud/v1/ayah/262"
response = requests.get(complete_url)
q = response.json()
print (q['data']['text'])


reshaped_text = arabic_reshaper.reshape(q['data']['text'])

#Convert left-right to right-left
from bidi.algorithm import get_display
bidi_text = get_display(reshaped_text)


#########################################
FONT_NAME = "Calibri"
FONT_SIZE = 20


   
# class in which we are creating the button by using boxlayout
# defining the App class
class BoxLayoutApp(App):
       
    def build(self):
 
        # To position oriented widgets again in the proper orientation
        # use of vertical orientation to set all widgets 
        superBox = BoxLayout(orientation ='vertical')
 
        # To position widgets next to each other,
        # use a horizontal BoxLayout.
        HB = BoxLayout(orientation ='horizontal')

#Prayer Times
        times = prayTimes.getTimes(date.today(), (32.9628, -117.0359),-7);
        p_time =""
        for i in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha', 'Midnight']:
            #print(i + ': ' + times[i.lower()])
            p_time = p_time+"\n"+i + ': ' + times[i.lower()]
         
        #btn1 = Button(text ="Prayer Times")
        btn1 = Button(text = p_time, font_name = FONT_NAME,font_size = FONT_SIZE)

#Weather
        btn2 = Button(text ="Weather")
          
        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found

        if x["cod"] != "404":
         
            # store the value of "main"
            # key in variable y
            y = x["main"]
         
            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]
         
            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]
         
            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]
         
            # store the value of "weather"
            # key in variable z
            z = x["weather"]
         
            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]
         
            # print following values
            '''
            print(" Temperature (in Celsius) = " +
                            str(current_temperature -273.15) +
                  "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                  "\n humidity (in percentage) = " +
                            str(current_humidity) +
                  "\n description = " +
                            str(weather_description))
            '''
            temperature = current_temperature -273.15
            humidity = current_humidity
            btn2 = Button(text = "Temperature : " + str(float("{:.2f}".format(temperature))) + "\n" + "Humidity : " + str(humidity), font_name = FONT_NAME,font_size = FONT_SIZE)
        else:
            print(" City Not Found ")
        
#Stock
        btn3 = Button(text ="QCOM SR : "+ str(stock['Stock Price']), font_name = FONT_NAME,font_size = FONT_SIZE)
        
#Currency_Exchange
        btn4 = Button(text ="USD to INR :" + str(float("{:.2f}".format(c_e["conversion_rates"]["INR"]))), font_name = FONT_NAME,font_size = FONT_SIZE)
 
        # HB represents the horizontal boxlayout orientation
        # declared above
        HB.add_widget(btn1)
        HB.add_widget(btn2)
        HB.add_widget(btn3)
        HB.add_widget(btn4)
 
        # To position widgets above/below each other,
        # use a vertical BoxLayout.
        VB = BoxLayout(orientation ='vertical')
 
#Quran
        btn5 = Button(text = bidi_text, font_name = 'Arial',font_size = FONT_SIZE)
        btn6 = Button(text ="Trivia")
        btn7 = Button(text ="Football")
        btn8 = Button(text ="News")
 
        # VB represents the vertical boxlayout orientation
        # declared above
        VB.add_widget(btn5)
        VB.add_widget(btn6)
        VB.add_widget(btn7)
        VB.add_widget(btn8)
 
        # superbox used to again align the oriented widgets
        superBox.add_widget(HB)
        superBox.add_widget(VB)
 
        return superBox
 
# creating the object root for BoxLayoutApp() class 
Box = BoxLayoutApp()

prayTimes = prayer_times.PrayTimes()

#print('Prayer Times for today in San Diego/USA\n' + ('=' * 41))
#print('Date :',date.today())

        
        


   
# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
Box.run()

#-------------------------- Test Code --------------------------

    
