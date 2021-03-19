# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:52:46 2021

@author: Sai Krishna
"""

#Importing library (pip install wikipedia)
import wikipedia

#Serach for the article. As exact article name is to be given for a summary, 
#it is good to start with search
print(wikipedia.search('Sachin'))

#Select the best page to get the summary
print(wikipedia.summary('Sachin'))

#If a shorter summary is required
print(wikipedia.summary("Sachin", sentences = 2))

#Getting URL
print(wikipedia.page('Sachin').url)

#Getting references
print(wikipedia.page("Sachin").references)
