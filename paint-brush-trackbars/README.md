# Paint Brush with Trackbars
## What it does
It allows you to draw brush paths in the openCV window area and choose the color/width of the path from the trackbars.
Pressing the 'c' key will clean the canvas.

## Where it comes from
The original script corresponds to the demo in the *Trackbar as the Color Palette* article of the 
openCV documentation:
https://docs.opencv.org/master/d9/dc8/tutorial_py_trackbar.html

## Improvements implemented
1. As the exercise, at the bottom of the article, suggested, I implemented a simple paint aplication. 
Taking the rgb values from the trackbars, and adding an extra bar for the width.

2. Added the functionality to clean the canvas through the 'c' key.

## Observations
Because of the fast movement of the pointer, I needed to join points with a path. First I tried to join them with  
a series of circles, which number depended of the distance between the original points, but I still ended up with blank spaces.
Then I tried joining them with a line path, which was easier and looked perfectly. So I went for the last approach.
