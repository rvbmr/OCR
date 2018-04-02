# Analysis on videos and analysis on images is very very similar bcz video breaks down to frames and frames are just like images

import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    
#    cv2.imshow('frame',frame)
    cv2.imshow('frame',cv2.resize(frame,(400,400)))    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()






