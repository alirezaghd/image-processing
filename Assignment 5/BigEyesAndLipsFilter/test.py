import cv2
import numpy as np
fruit = ['apple', ' banana', 'orang']

for i, fruits in enumerate(fruit):
    print(i ,fruit)

image = np.zeros((200,300), dtype=np.uint8)
point = np.array([[3,40],[140,7],[40,240],[50,120]], dtype=int)

cv2.drawContours(image,[point],-1,(255,255,255),-1)

cv2.imshow("out",image)
cv2.waitKey()