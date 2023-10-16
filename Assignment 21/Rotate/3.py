import cv2
import numpy as np

image = cv2.imread('3.jpg',0)

height, width = image.shape

rotated_image = np.zeros((height, width, 1), dtype=np.uint8)


for i in range(height):
    for j in range(width):
        rotated_image[i, j] = image[height - i - 1, width - j - 1]
       
cv2.imshow('show output',image)
cv2.imshow('Rotated Image', rotated_image)

cv2.waitKey()