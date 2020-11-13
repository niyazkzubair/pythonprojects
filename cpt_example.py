# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:09:22 2020

@author: nzubair
"""
from cpt.cpt import Cpt
model = Cpt()

###1
model.fit([
            ['hello', 'world'],
            ['hello', 'world'],
            ['hello', 'world'],
            ['hello', 'world'],
            ['hello', 'this', 'is', 'me'],
            ['hello', 'me']
          ])

#print (model.compute_noisy_items(0.3))
#print (model.predict([['hello'], ['hello', 'this']])) #worked
#print (model.predict([['hello'],['this']]))
print (model.predict([['hello']]))
# Output: ['me', 'is']
