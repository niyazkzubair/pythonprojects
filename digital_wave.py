# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:04:25 2020

@author: nzubair
"""

import numpy as np
import matplotlib.pyplot as plt

data = [1, 0.5, 0, 0, 1, 0, 1, 0]
xs = np.repeat(range(len(data)), 2)
ys = np.repeat(data, 2)
xs = xs[1:]
ys = ys[:-1]
plt.plot(xs, ys)
plt.ylim(-0.5, 1.5)
plt.show()

def updatecursorposition(event):
    '''When cursor inside plot, get position and print to statusbar'''
    if event.inaxes:
        x = event.xdata
        y = event.ydata
        statbar.push(1, ("Coordinates:" + " x= " + str(round(x,3)) + "  y= " + str(round(y,3))))

def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

bits = [0,1,1,1,0,0,1,1,1,0,0,1,0]
data = np.repeat(bits, 2)
clock = 1 - np.arange(len(data)) % 2
manchester = 1 - np.logical_xor(clock, data)
t = 0.5 * np.arange(len(data))

#plt.hold(True)
my_lines('x', range(2000), color='.5', linewidth=0.5)
my_lines('y', [0.5, 2, 4], color='.5', linewidth=0.5)
plt.step(t, clock + 4, 'r', linewidth = 2, where='post')
plt.step(t, data + 2, 'r', linewidth = 2, where='post')
plt.step(t, manchester, 'r', linewidth = 2, where='post')
plt.ylim([-1,6])

for tbit, bit in enumerate(bits):
    plt.text(tbit + 0.5, 1.5, str(bit))

plt.gca().axis('off')
plt.show()