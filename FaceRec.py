import numpy as np
import cv2
import matplotlib.pyplot as plt

def grab_frame(cap):
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#Initiate the camera
cap1 = cv2.VideoCapture(0)

#create two subplots
ax1 = plt.subplot(1,2,1)
ax2 = plt.subplot(1,2,2)

#create two image plots
im1 = ax1.imshow(grab_frame(cap1))
im2 = ax2.imshow(grab_frame(cap1))
plt.ion()

while True:
    im1.set_data(grab_frame(cap1))
    im2.set_data(grab_frame(cap1))
    plt.pause(0.001)

plt.ioff() # due to infinite loop, this gets never called.
plt.show()