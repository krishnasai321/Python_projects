# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:27:35 2021

@author: Sai Krishna
"""

#Importing libraries
import cv2
import os

#Setting directory
os.chdir('C:\\Data\\github\\python_projects\\Open CV\\Face detection')

#Using the frontalface xml file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_cascade.empty()

#Selecting original image
img = cv2.imread('sachin-tendulkar.jpg')

cv2.imshow("sachin", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Detection corners of face
faces = face_cascade.detectMultiScale(img, 1.1, 4)

#Creating a rectangle
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#Saving the image
cv2.imwrite("sachin_face_detected.png", img) 

cv2.imshow("sachin_face_detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
