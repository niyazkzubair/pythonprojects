# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:32:35 2020

@author: nzubair
"""
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav('file_example_WAV_1MG.wav')
play(sound)
