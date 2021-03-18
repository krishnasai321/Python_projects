# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:45:56 2021

@author: Sai Krishna
"""

#Import libraries (need to do pip install nsepy if not already done)
from nsepy import get_history
from datetime import datetime

#Date or dates for which stock information is required
date = datetime(2021, 3,18)

#Checking stock price for SBI bank
data = get_history(symbol = 'SBIN', start = date, end = date)
#Can use any required start and end dates

data

#If required for list of stocks
sym_list = ['BEL','L&TFH','TATAMOTORS','IOC','RITES','TITAN']

for sym in sym_list:
    data2 = get_history(symbol = sym, start = date, end = date)
    data = data.append(data2)
    
#Adding a %change metric
data['%Change'] = round(100*(data['Close']/data['Prev Close']-1),2)

data.head()
