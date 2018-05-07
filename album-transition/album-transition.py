#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:28:55 2018

@author: adilson
"""
import os
import numpy as np
import cv2 as cv

dir = './pics/'

# add slash to dir if it doesn't have it
if dir[-1] != '/':
    dir += '/'
    
# create a list of files inside 
files_list = os.listdir(dir)

# clean the list of unwanted files
# only .jpg, .png, .jpeg are valid
purged_list = []
valid_exts = ['jpg', 'jpeg', 'png']
for file in files_list:
    ext = file[file.rfind('.')+1:]
    if ext in valid_exts:
        purged_list.append(file)
files_list = purged_list

# start pic names and opening 
img1_name = files_list[0]
if len(files_list) == 1:
        img2_name = img1_name
else:
    img2_name = files_list[1]
    
img1 = cv.imread(dir + img1_name)
img2 = cv.imread(dir + img2_name)


# function that changes base pics for transition
def changeBasePics():
    global img1_name, img2_name, index, img1, img2 
    index += 1
    if len(files_list) == 1:
        img1_name = files_list[0]
        img2_name = img1_name
    elif index == len(files_list) - 1:
        img1_name = files_list[index]
        img2_name = files_list[0]     
        index = -1
    else:
        img1_name = files_list[index]
        img2_name = files_list[index+1] 
    #opening the pics files
    img1 = cv.imread(dir + img1_name)
    img2 = cv.imread(dir + img2_name)

# transition parameters
alpha = 1.0
step = 0.01
index = 0

#transition
while(True):

    imgs_added = cv.addWeighted(img1,alpha,img2,1.0-alpha, 0)
    cv.imshow('image', imgs_added)
    
    # calculating sinusoidal delay: function of alpha
    # wavelength = 1 (alpha value)
    # amplitude = 80 (goes from 90->20->90)
    t = (alpha*np.pi) + np.pi #getting a radian angle from pi to 2pi
    delay = (np.sin(t)+1)*80+20
    delay = int(delay)
    
    #calculating next alpha to use
    alpha -= step
    
    # end of the transition
    #chaning base pics and resetting alpha
    if alpha < 0:
        changeBasePics()
        alpha = 1.0
    
    # delay and waiting for key press
    if cv.waitKey(delay) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
        
    




