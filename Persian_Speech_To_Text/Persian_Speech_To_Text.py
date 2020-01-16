# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:27:24 2019

@author: Abdolkarim Saeedi
"""

import speech_recognition as sr

filename = sr.AudioFile('myfile.wav')
r = sr.Recognizer()
with filename as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
print(r.recognize_google(audio, language = 'fa-IR', show_all = True ))