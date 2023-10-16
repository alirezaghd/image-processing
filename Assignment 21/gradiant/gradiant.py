import cv2
import numpy as np


width, height = 400, 400  # ابعاد تصویر
image = np.ones((height, width, 1), np.uint8)

for i in range(height):
    gradiant = i / height * 255
    image[i, :] = gradiant

cv2.imwrite('gradiant.jpg',image)
cv2.imshow('photo',image) 
cv2.waitKey()