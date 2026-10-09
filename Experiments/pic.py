import numpy as np
import cv2 as cv
import os 
import pathlib
from time import sleep

calls = 0

randomM = np.random.rand(1600,1200,3) * 20 - 10
M = np.zeros((1600,1200,3))
M[::10,:,:] = -255
M[:,::10,:] = -255

def glitch(event,x,y,flags,param):
    global img, Rout, Gout, Bout, RG, GB, RB, calls, randomM

    if event == cv.EVENT_MOUSEMOVE: 
        if calls % 7 == 0:
            cv.imshow("image", Rout)
        elif calls % 5 == 0:
            cv.imshow("image", Gout + M)
        elif calls % 3 == 0:
            cv.imshow("image", Bout)
        elif calls % 2 == 0:
            cv.imshow("image", RG + M)
        else:
            cv.imshow("image", RB)
        calls = calls + 1

img = cv.imread('casa.jpeg')
Z = np.zeros(img.shape[:2])
Rout = np.stack((img[:,:,0],Z,Z), axis = -1)
Gout = np.stack((Z,img[:,:,1],Z), axis = -1)
Bout = np.stack((Z,Z,img[:,:,2]), axis = -1)
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
RG = np.stack((R,G,Z), axis = -1)
GB = np.stack((Z,G,B), axis = -1)
RB = np.stack((R,Z,B), axis = -1)
assert img is not None, "file could not be read, check with os.path.exists()"


cv.namedWindow('image')

cv.imshow("image", img)

cv.setMouseCallback('image',glitch)

cv.waitKey(0)           # Wait until a key is pressed
cv.destroyAllWindows()  
