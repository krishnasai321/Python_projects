# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:49:40 2021

@author: Sai Krishna
"""

#Importing libraries (pip install googletrans==3.1.0a0)
#use this version or check for latest version if code throws nonetype error
import googletrans

#Checking all supported languages
print(googletrans.LANGUAGES)
#en - english, hi - hindi, te - telugu, es - spanish

#importing translator module
from googletrans import Translator
translator = Translator()

#Entering just english word without and dest gives english word
result = translator.translate('I love you')
print(result.src)
print(result.dest)
print(result.origin)
print(result.text)

result = translator.translate('I love you',dest = 'hi')
print(result.text)

result = translator.translate('I love you',dest = 'te')
print(result.text)

result = translator.translate('I love you',dest = 'es')
print(result.text)

#With a known source
result = translator.translate('Te quiero', src='es')
print(result.src)
print(result.dest)
print(result.origin)
print(result.text)