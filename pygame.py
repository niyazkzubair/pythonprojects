# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:15:04 2020

@author: nzubair
"""
#import cv2  
import numpy as np
import matplotlib.pyplot as plt

'''
image = np.zeros((256,256), np.uint8)
thickness = np.random.randint(1,5, size=(1,1))

for i in range (10):
    tol = np.random.randint(0,3, size=(1,1))
    
    if(tol==0):
        start_x = np.random.randint(low=0, high=255, size=(1,1))
        start_y = np.random.randint(low=0, high=255, size=(1,1))
        end_x = np.random.randint(low=0, high=255, size=(1,1))
        end_y = np.random.randint(low=0, high=255, size=(1,1))
    if(tol==1):
        start_x = np.random.randint(low=0, high=255, size=(1,1))
        start_y = np.random.randint(low=0, high=255, size=(1,1))
        end_x = start_x
        end_y = np.random.randint(low=0, high=255, size=(1,1))
    if(tol==2):
        start_x = np.random.randint(low=0, high=255, size=(1,1))
        start_y = np.random.randint(low=0, high=255, size=(1,1))
        end_x = np.random.randint(low=0, high=255, size=(1,1))
        end_y = start_y
    
    start_point = (start_x, start_y) 
    end_point = (end_x,end_y) 
    color = 255
  
    image = cv2.line(image, start_point, end_point, color, int(thickness)) 
  
# Displaying the image  
plt.imshow(image)
np.savetxt('PIXEL_PATTERN.txt', image, fmt="%x")   

  
# data to be plotted 
x = np.arange(1, 256)  
y = x * x 
  
# plotting 
plt.title("Line graph")  
plt.xlabel("X axis")  
plt.ylabel("Y axis")  
plt.plot(x, y, color ="red")   
plt.imshow()
'''
def fig2data ( fig ):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw ( )
 
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = numpy.fromstring ( fig.canvas.tostring_argb(), dtype=numpy.uint8 )
    buf.shape = ( w, h,4 )
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = numpy.roll ( buf, 3, axis = 2 )
    return buf

def fig2img ( fig ):
    """
    @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
    @param fig a matplotlib figure
    @return a Python Imaging Library ( PIL ) image
    """
    # put the figure pixmap into a numpy array
    buf = fig2data ( fig )
    w, h, d = buf.shape
    return Image.fromstring( "RGBA", ( w ,h ), buf.tostring( ) 

 
# Generate a figure with matplotlib</font>
figure = plt.figure()
plot   = figure.add_subplot ( 111 )
 
# draw a cardinal sine plot
x = np.arange ( 0, 100, 0.1 )
y = np.sin ( x ) / x
plot.plot ( x, y )
plt.show()

im = fig2img ( figure )
im.show()