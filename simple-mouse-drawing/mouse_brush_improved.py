#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 19:53:55 2018

@author: adilson
"""

import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed
mode = True # if True, draw a rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
saved = np.zeros((512,512,3), np.uint8)

#clear screen function
def save_screen():
    global saved
    saved = np.array(img)
    

def restore_saved():
    global img
    img = np.array(saved)
    


# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix, iy, drawing, mode
    
    if event == cv.EVENT_LBUTTONDOWN:
        save_screen()
        drawing = True
        ix, iy = x,y
        
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            restore_saved()
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,200,0),3)
            else:
                radius = int(np.sqrt((x-ix)**2+(y-iy)**2))
                cv.circle(img,(ix,iy),radius,(0,0,200),3)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,200,0),3)
        else:
            radius = int(np.sqrt((x-ix)**2+(y-iy)**2))
            cv.circle(img,(ix,iy),radius,(0,0,200),3)
            
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while(True):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('c'): # clear screen
        img = np.zeros((512,512,3), np.uint8)
    elif k == 27:
        break
cv.destroyAllWindows()


            
            
            
            
            
            
            
            
            
            
            
            