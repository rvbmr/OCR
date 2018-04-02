import cv2
import numpy as np
import matplotlib.pyplot as plt
#								0
img = cv2.imread('Manas.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

cv2.imshow('image',cv2.resize(img,(300,400)))
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image',300,400)

cv2.waitKey(0)
cv2.destroyAllWindows()

