# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:27:24 2019

@author: Abdolkarim Saeedi
"""

import speech_recognition as sr

# load desired audio file
# or use mic to do recognition simultaneously

filename = sr.AudioFile('myfile.wav')

# create a recognizer instance

r = sr.Recognizer()

# open the audio file

with filename as source:
    
    # denoise the file for better precision
    
    r.adjust_for_ambient_noise(source)
    
    # read from data
    
    audio = r.record(source)
    
# perform recognition and see the results

print(r.recognize_google(audio, language = 'fa-IR', show_all = True ))
