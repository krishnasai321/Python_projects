# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 00:19:39 2021

@author: Sai Krishna
"""

#Importing pyttsx3 (pip install pyttsx3)
import pyttsx3

#initialization
engine = pyttsx3.init()

#String or text to be converted to speech
string = "I like Python. Hope you have a great day ahead."

#Convert to speech
engine.say(string)
engine.runAndWait()