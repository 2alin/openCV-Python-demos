#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:20:28 2018

@author: adilson
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

font = cv.FONT_HERSHEY_COMPLEX_SMALL
height = 400
width = 400
n = 30

def generate_data():
    trainData = np.random.randint(30,height,(n,2)).astype(np.float32)
    
    return trainData

def label_data():
    responses = np.random.randint(0,2,(n,1)).astype(np.float32)
    return responses

def plot_data():
    global img
    for k in range(n):
        x, y = trainData[k,:]
        x, y = int(x), int(y)
        if responses[k] == 0:
            color = (255,0,0)
        else:
            color = (0,0,255)
#        print("plotting")
        cv.rectangle(img, (x,y), (x+8,y+8), color,-1)
    return None

#mouse callback function
def draw_line(event,x,y,flags,param):
    global startDraw, p1, p2, mode, img_line, img_newcomers
    if event == cv.EVENT_LBUTTONDOWN:
        if startDraw:
            startDraw = False
            p2 = x,y
#            print(p1,p2)
            cv.rectangle(img_line, (0,0), (width,28), (255,255,255),-1)
            cv.putText(img_line, 'Newcomers path', (10,25), font,0.9, 
               (0,0,0),1,cv.LINE_AA)
            cv.line(img_line, p1, p2,(0,255,0),2)
            mode = 1
            
        else:
            img_line = np.copy(img)
            img_newcomers = np.copy(img)
            startDraw = True
            p1 = x,y
            mode = 0

def get_newcomers():
    x1,y1 = p1
    x2,y2 = p2
    nX = int(np.abs(x1-x2)/20)
    nY = int(np.abs(y1-y2)/20)
    n = max(nX,nY)
    newcomers = zip(np.linspace(x1,x2,n+1), np.linspace(y1,y2,n+1))
    newcomers = np.array(list(newcomers), np.uint16)
    return newcomers

def plot_newcomers(newcomers):
    cv.rectangle(img_newcomers, (0,0), (width,28), (255,255,255),-1)
    cv.putText(img_newcomers, 'Newcomers added', (10,25), font,0.9, 
               (0,0,0),1,cv.LINE_AA)
    for point in newcomers:
        cv.rectangle(img_newcomers, (point[0],point[1]), (point[0]+8,point[1]+8), 
                     (0,255,0),-1)
    
# create a black image, a window and bind the function to window
img = np.zeros((height,width, 3), np.uint8)
img +=255
cv.namedWindow('image')
cv.moveWindow('image', 800,250)
cv.setMouseCallback('image', draw_line)

startDraw = False
mode = 0
p1 = (0,0)
p2 = (0,0)

img_line = np.copy(img)
img_newcomers = np.copy(img)
trainData = generate_data()
responses = label_data()
plot_data()

knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)

while(True):
    if mode==1:
        cv.imshow('image', img_line)
    elif mode == 2:
        cv.imshow('image', img_newcomers)
    else:
        cv.imshow('image', img)        
#        print("showing img")
    k = cv.waitKey(20) & 0xFF
    if k == ord('q'):
        break
    elif k == ord('c'):
        mode = 2
        newcomers = get_newcomers()
        plot_newcomers(newcomers)
    elif k == ord('d'):
        mode = 0
        newcomers = np.array(newcomers, np.float32)
        ret, results, neighbours, dist = knn.findNearest(newcomers,3)
#        print(results)
        trainData = np.vstack([trainData, newcomers])
        responses = np.vstack([responses, results])
        n = len(responses)
        plot_data()
        cv.rectangle(img, (0,0), (width,28), (255,255,255),-1)
        cv.putText(img, 'Newcomers classified', (10,25), font,0.9, 
               (0,0,0),1,cv.LINE_AA)
        knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
    elif k == ord('n'):
        # reset simulation
        n = 30
        img = np.zeros((height,width, 3), np.uint8)
        img +=255
        img_line = np.copy(img)
        img_newcomers = np.copy(img)
        trainData = generate_data()
        responses = label_data()
        plot_data()
        knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
        cv.rectangle(img, (0,0), (width,28), (255,255,255),-1)
        cv.putText(img, 'Reset simulation', (10,25), font,0.9, 
               (0,0,0),1,cv.LINE_AA)
               
            
cv.destroyAllWindows()