# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 23:36:06 2021

@author: Sai Krishna
"""

#Setting directory for download location
import os
os.chdir('C:\\Data\\github\\python_projects\\Youtube video downloader')

#Importing pytube (use pip install pytube)
from pytube import YouTube

#Video link as a string
link = "https://www.youtube.com/watch?v=8b0ubLO2MUE"

video = YouTube(link)

#Using the best resolution option
stream = video.streams.get_highest_resolution()

#File name of the video about to be downloaded
stream.default_filename

#Video Resolution
stream.resolution

#Title of the video
stream.title

#Download command
stream.download()
