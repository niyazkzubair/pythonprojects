# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:00:25 2020

@author: nzubair
"""

import winsound

winsound.Beep(1000, 2000)
winsound.Beep(2000, 2000)
winsound.Beep(3000, 2000)
winsound.Beep(4000, 2000)
winsound.Beep(5000, 2000)
winsound.Beep(6000, 2000)
winsound.Beep(7000, 2000)
winsound.Beep(8000, 2000)
winsound.Beep(9000, 2000)
winsound.Beep(10000, 2000)

# Play Windows exit sound.
#winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
winsound.PlaySound("file_example_WAV_1MG.wav", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("*", winsound.SND_ALIAS)