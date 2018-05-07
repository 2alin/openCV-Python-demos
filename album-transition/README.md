# Album Transition
## What it does
It transitions over all the pictures in an directory with a smooth effect. Use 'q' to exit the transition.

## Where it comes from
This is an original approach to the exercise suggested at the bottom of this article:
https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html

## Requirements
1. To have openCV python library properly installed.
2. Put all the pictures that you want to transition in a folder called 'pics' in the same parent directory than the script.
3. There's no specific dimension needed for the pictures. But all of them should share the same dimension, otherwise the script won't work.

## Highlights
1. The script is able to recognize the pictures with extensions `.png .jpg .jpeg` and ignore all other kind of files.

2. The transition effect is not linear. Instead uses a sinusoidal function that makes the beginning and ending of each transition 
(where the pic is full displayed)longer than the the middle of the transition (where the pictures are overlapped). This is a graph
of the transition delay function I used:

![plot of the transition delay function](https://github.com/2alin/openCV-demos/blob/master/album-transition/assets/delay_plot.png)

## Akcnowledgements
The pictures I take as a sample for the script are from  Schalk Neethling's [unsplash album](https://unsplash.com/@schalkneethling).
