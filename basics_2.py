# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:49:42 2020

@author: nzubair
"""

import numpy as np
import scipy.constants

print (np.ones((2, 3), dtype = np.int))
print (np.zeros((3,3)))

np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size) #Total number of entries


print("dtype:", x3.dtype)
print("itemsize:", x3.itemsize, "bytes") #Size of each entry in bytes
print("nbytes:", x3.nbytes, "bytes") #Total size of array in bytes


print(x2[:2, :3])
print(x2[:3, ::2]) #all rows, every other column
print(x2[:, 0])  # first column of x2
print(x2[0, :])  # first row of x2

###Copy
x2_sub_copy = x2[:2, :2].copy()

###Reshaping
grid = np.arange(1, 10).reshape((3, 3))
print(grid)

grid.reshape(1,9)

###Concatenation
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.concatenate([x, y])

###Split
#1D
p = [1, 2, 3, 99, 99, 3, 2, 1]
p1, p2, p3 = np.split(p, [3, 5])
print(p1, p2, p3)

#Horizontal split
grid = np.arange(16).reshape((4, 4))
print (grid)
upper, lower = np.vsplit(grid, [2])
left, right = np.hsplit(grid, [2])
#Vertical split


###Matrix
mat_1 = np.matrix('1 2; 3 4')
mat_3 = mat_1.T


################### SciPy ###############
##Constants
print ("PI : ",scipy.constants.pi)

##FFT
from scipy.fftpack import fft
#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
print (y)

def my_function():
  print("Hello from a function")

my_function()
