# Simple Mouse-Drawing
## What it does
It allows you to draw circles and squares in the openCV window area, dragging while mouse left button is pressed. 
Pressing the 'm' key will togle the shape to draw.

## Where it comes from
The original script corresponds to the advaned demo (bottom of the page) in the *Mouse as a Paint-Brush* section of the 
openCV documentation:
https://docs.opencv.org/master/db/d5b/tutorial_py_mouse_handling.html

## Improvements implemented
1. I added a couple of functions that allowed the demo to make the drawing interactive. 
The original demo kept drawing shape over shape when the cursor was moving, making the result figure a complete mess.
My script removes previous shapes when the cursor is moving, then save the canvas state when the cursor is released,
and when drawing starts again the script draws the saved figure over and over, removing unwanted dragging shapes.

2. Circle radius is now interactive, taking into account the start position (click) as center 
and the end position (release) as the delimiter of the radious. The original demo only was able to draw fixed size circles.

3. Added the functionality to clean the canvas through the 'c' key.


