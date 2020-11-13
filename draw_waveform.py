# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:48:56 2020

@author: nzubair
"""

#https://github.com/wallento/wavedrompy

import wavedrom
svg = wavedrom.render("""
{ "signal": [
 { "name": "CK",   "wave": "P.......",                                              "period": 2  },
 { "name": "CMD",  "wave": "x.3x=x4x=x=x=x=x", "data": "RAS NOP CAS NOP NOP NOP NOP", "phase": 0.5 },
 { "name": "ADDR", "wave": "x.=x..=x........", "data": "ROW COL",                     "phase": 0.5 },
 { "name": "DQS",  "wave": "z.......0.1010z." },
 { "name": "DQ",   "wave": "z.........5555z.", "data": "D0 D1 D2 D3" }
]}""")
svg.saveas("demo1.svg")