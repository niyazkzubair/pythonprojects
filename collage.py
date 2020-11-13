# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:41:03 2020

@author: nzubair
"""

import sys
from PIL import Image



size = 192,192
im1 = Image.open('1.jpg')
im1.thumbnail(size,Image.ANTIALIAS)
im1.save('1_t.jpg')


im1 = Image.open('2.jpeg')
im1.thumbnail(size,Image.ANTIALIAS)
im1.save('2_t.jpeg')


im1 = Image.open('3.jpeg')
im1.thumbnail(size,Image.ANTIALIAS)
im1.save('3_t.jpeg')



images = [Image.open(x) for x in ['1_t.jpg', '2_t.jpeg', '3_t.jpeg']]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

#new_im = Image.new('RGB', (total_width, max_height))
new_im = Image.new('RGB', (1440, 2560))
new_im.save('test_new.jpg')

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test.jpg')

