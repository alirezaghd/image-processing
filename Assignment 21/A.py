import cv2
import numpy as np


width, height = 400, 400  # ابعاد تصویر
image = np.ones((height, width, 1), np.uint8) * 255

image[120:190,180:190] = 0
image[120:190,220:230] = 0

image[120:130,180:230] = 0
image[150:160,180:230] = 0


cv2.imwrite('A.jpg',image)
cv2.imshow('photo',image) 
cv2.waitKey()