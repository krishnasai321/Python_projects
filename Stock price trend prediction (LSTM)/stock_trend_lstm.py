# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:09:27 2021

@author: Sai Krishna
"""

#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler

#Setting direcory
os.chdir('C:\\Data\\github\\Python_projects\\Stock price trend prediction (LSTM)')

#Getting data
df=pd.read_csv('NSE-Tata-Global-Beverages-Limited.csv')
df.head()

#Changin data and some preprocessing steps
df['Date']=pd.to_datetime(df.Date,format="%Y-%m-%d")
df.index=df['Date']
plt.figure(figsize=(16,8))
plt.plot(df["Close"],label='Close Price history')

#Sorting data and creating new dataset
data=df.sort_index(ascending=True,axis=0)
new_dataset=pd.DataFrame(index=range(0,len(df)),columns=['Date','Close'])
for i in range(0,len(data)):
    new_dataset["Date"][i]=data['Date'][i]
    new_dataset["Close"][i]=data["Close"][i]
    
#Min_max scalar
scaler=MinMaxScaler(feature_range=(0,1))
new_dataset.index=new_dataset.Date
new_dataset.drop('Date',axis=1,inplace=True)
final_dataset=new_dataset.values

#Appropriate training and validation data
train_data=final_dataset[0:987,:]
valid_data=final_dataset[987:,:]

#Scaling data
scaled_data=scaler.fit_transform(final_dataset)

x_train_data,y_train_data=[],[]

#Adding lot of lag values which means we have lot of columns for training
for i in range(60,len(train_data)):
    x_train_data.append(scaled_data[i-60:i,0])
    y_train_data.append(scaled_data[i,0])
    
x_train_data,y_train_data=np.array(x_train_data),np.array(y_train_data)
x_train_data=np.reshape(x_train_data,(x_train_data.shape[0],x_train_data.shape[1],1))

#LSTM models
lstm_model=Sequential()
lstm_model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train_data.shape[1],1)))
lstm_model.add(LSTM(units=50))
lstm_model.add(Dense(1))

lstm_model.compile(loss='mean_squared_error',optimizer='adam')
lstm_model.fit(x_train_data,y_train_data,epochs=10,batch_size=1,verbose=2)

#Predict on test data
inputs_data=new_dataset[len(new_dataset)-len(valid_data)-60:].values
inputs_data=inputs_data.reshape(-1,1)
inputs_data=scaler.transform(inputs_data)

X_test=[]
for i in range(60,inputs_data.shape[0]):
    X_test.append(inputs_data[i-60:i,0])
X_test=np.array(X_test)
X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
predicted_closing_price=lstm_model.predict(X_test)
predicted_closing_price=scaler.inverse_transform(predicted_closing_price)

train_data=new_dataset[:987]
valid_data=new_dataset[987:]
valid_data['Predictions']=predicted_closing_price

#Plotting
plt.plot(train_data["Close"])
plt.plot(valid_data[['Close',"Predictions"]])

