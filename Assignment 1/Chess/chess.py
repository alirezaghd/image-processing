import cv2
import numpy as np

array = np.zeros((800,800,1))


for i in range(800):
    for j in range(800):
        
        x= (i//100)% 2
        y= (j//100)% 2

        if (x%2 == 0 and y%2 == 0) or (x%2 == 1 and y%2 == 1):
            array[i][j] = 255

        else:
           array[i][j] = 0

print(array)
#cv2.imwrite('chess1.jpg',array)
cv2.imshow('photo',array) 
cv2.waitKey()