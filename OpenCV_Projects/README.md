## Hand Gesture Recognition

This program recognizes numerical hand gestures from 1 to 5. The algorithm followed is shown below. 
It uses OpenCV for morphological transformation and thresholding to separate the image of the hand
from the background. To exit the program press "Q".
\
\
Open Camera\
Capture frames from the camera\
Get hand data from the rectangle sub window\
Apply Gaussian blur\
Change color-space from BGR -> HSV\
Create a binary image with where white will be skin colors and rest is black\
Kernel for morphological transformation\
Apply morphological transformations to filter out the background noise\
Apply Gaussian Blur and Threshold\
Show threshold image\
Find contours\
Find contour with maximum area\
Create bounding rectangle around the contour\
Find convex hull\
Draw contour\
Find convexity defects\
Use cosine rule to find angle of the far point from the start and end point i.e. the convex points (the finger\
tips) for all defects\
if angle > 90 draw a circle at the far point\
Print number of fingers\
Show required images\
Close the camera if 'q' is pressed
