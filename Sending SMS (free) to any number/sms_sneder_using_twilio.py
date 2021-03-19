# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:45:17 2021

@author: Sai Krishna
"""

#Importing required modules from twilio package (pip install twilio)
from twilio.rest import Client

#Create free trial twilio account.
#Get the account sid and auth token
#Create a free trial number using trial balance

#Changin the sid/auth tokens from actuals for privacy reasons
account_sid = 'ACarr145659c7f6b4fcb2978rd74971101'
auth_token = '2095967dcrb09620fma16ff5t4db402e'

#Initiating the Client
client = Client(account_sid, auth_token)

#Sending message
#Use free trial number from twilio in from_
#Use any number with country code in to
message = client.messages.create(body='Hi there! How are you?', from_=[+15595001013],to = [+917602518817])

# printing the sid after success
print(message.sid)

#MSG received!