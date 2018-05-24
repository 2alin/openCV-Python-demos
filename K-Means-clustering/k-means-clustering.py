#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:30:43 2018

@author: adilson
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

font = cv.FONT_HERSHEY_COMPLEX_SMALL
height = 400
width = 400

# Turn interactive plotting off
plt.ioff()

# Define criteria
criteria = (cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)

#set flags
flags = cv.KMEANS_RANDOM_CENTERS


def generate_data():
    centers = [(np.random.randint(1,400), np.random.randint(1,400)) for k in range(4)]

    raw = [[(pair[0]+np.random.randint(1,61), pair[1]+np.random.randint(1,61)) 
            for k in range(10)]for pair in centers]
    raw = np.array(raw)
    
    points = raw.reshape((40,2))
    points = np.float32(points)
    return points

def change_mode(event,x,y,flags,param):
    global mode, img, A, B, C, D, compactness, labels, centers, points, h, w, margin
    if event == cv.EVENT_LBUTTONDOWN:
        mode += 1
        mode = mode%3
        if mode == 1:
            print("calculate centroids")
            #clear plot
#            plt.gcf().clear()
            #plot
            plt.scatter(centers[:,0],centers[:,1], marker = 'X', c='cyan', alpha=1.0, s=70)
            #save img
            plt.savefig('temp.png', bbox_inches='tight')
            #load img
            img = cv.imread('temp.png')
            #add margin to img
            img = np.vstack([margin,img])
            
            #add header
            cv.rectangle(img, (0,0), (w,30), (255,255,255),-1)
            cv.putText(img, 'Centroids', (10,25), font,0.9, 
               (0,0,0),1,cv.LINE_AA)
            
        elif mode == 2:
            print("clustering")
            #clear plot
            plt.clf()
            
            #plot
#            plt.axis([0,450,0,450])
            plt.scatter(A[:,0],A[:,1], marker = 'o', c='r', alpha=0.5, s=70)
            plt.scatter(B[:,0],B[:,1], marker = 'o', c='b', alpha=0.5,s=70)
            plt.scatter(C[:,0],C[:,1], marker = 'o', c='y', alpha=0.5, s=70)
            plt.scatter(D[:,0],D[:,1], marker = 'o', c='g', alpha=0.5, s=70)
            plt.scatter(centers[:,0],centers[:,1], marker='X', c='cyan', alpha=0.5, s=70)
            
            #save plot
            plt.savefig('temp.png', bbox_inches='tight')
            
            #load img
            img = cv.imread('temp.png')
            #get widht and height of img
            h,w = img.shape[:2]
            
            #add top margin 28 px
            margin = np.zeros((28,w,3), np.uint8)
            margin +=255
            #add margin to img
            img = np.vstack([margin,img])

            
            cv.rectangle(img, (0,0), (w,30), (255,255,255),-1)
            cv.putText(img, 'Clustering', (10,25), font,0.9, 
               (0,0,0),1,cv.LINE_AA)
        else:
            print("reset data")
            #clear plot
            plt.clf()
            
            #generate data
            points = generate_data()
            
            #Apply KMeans
            labels = 0
            compactness,labels,centers  = cv.kmeans(points,4,None,criteria,10,flags)
            A = points[labels.ravel()==0]
            B = points[labels.ravel()==1]
            C = points[labels.ravel()==2]
            D = points[labels.ravel()==3]
            
#            plt.axis([0,450,0,450])
            plt.scatter(points[:,0],points[:,1], marker = 'o', c='black', alpha=0.5, s=70)
            plt.savefig('temp.png', bbox_inches='tight')

            #load img
            img = cv.imread('temp.png')
            #get widht and height of img
            h,w = img.shape[:2]
            
            #add top margin 28 px
            margin = np.zeros((28,w,3), np.uint8)
            margin +=255
            #add margin to img
            img = np.vstack([margin,img])
            
            #add label
            cv.rectangle(img, (0,0), (w,30), (255,255,255),-1)
            cv.putText(img, 'Reset Data', (10,25), font,0.9, 
               (0,0,0),1,cv.LINE_AA)
    return None 


mode = 0
points = generate_data()
#plot original data
plt.figure(figsize=(8,5))
#plt.axis([0,450,0,450])
plt.scatter(points[:,0],points[:,1], marker = 'o', c='black', alpha=0.5, s=70)
plt.savefig('temp.png', bbox_inches='tight')

#Apply KMeans
compactness,labels,centers  = cv.kmeans(points,4,None,criteria,10,flags)
A = points[labels.ravel()==0]
B = points[labels.ravel()==1]
C = points[labels.ravel()==2]
D = points[labels.ravel()==3]

#load plot as figure
img = cv.imread('temp.png')
#get widht and height of img
h,w = img.shape[:2]

#add top margin 28 px
margin = np.zeros((28,w,3), np.uint8)
margin +=255

#add margin to img
img = np.vstack([margin,img])


# create a white image, a window and bind the function to window
#img = np.zeros((h,w, 3), np.uint8)
#img +=255
cv.namedWindow('image')
cv.moveWindow('image', 800,250)
cv.setMouseCallback('image', change_mode)



while(True):
    cv.imshow('image',img)
    k = cv.waitKey(100) & 0xFF
    if k == ord('q'):
        print('quit')
        break
    
cv.destroyAllWindows()