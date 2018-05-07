#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 23:42:07 2018

@author: adilson
"""

import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed
px, py = -1, -1

# link two points with a series of circles
def link_points(px,py,x,y):
    cv.line(img,(px,py),(x,y),(b,g,r),2*width,cv.LINE_AA)
        
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global px,py, drawing
    
    if width == 0:# avoid console errors
        return
    
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        px, py = x, y
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            link_points(px,py,x,y)
            cv.circle(img,(x,y),width,(b,g,r),-1,cv.LINE_AA)
            px, py = x, y
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),width,(b,g,r),-1,cv.LINE_AA)

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((500,800,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

#create trackbars for color change
cv.createTrackbar('R','image',10,255,nothing)
cv.createTrackbar('G','image',100,255,nothing)
cv.createTrackbar('B','image',200,255,nothing)

#create trackbar for brush radius
cv.createTrackbar('Width','image',4,50,nothing)
    
while(True):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('c'): # clear screen
        img = np.zeros((500,800,3), np.uint8)
    
    # get current positions of all trackbars
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    width = cv.getTrackbarPos('Width', 'image')    

cv.destroyAllWindows()
    










