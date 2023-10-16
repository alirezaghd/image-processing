import cv2
import numpy as np

img = cv2.imread("p.png",0)

x=0
for i in range(130):
    img[135-x:137-x,0+x:40+x] = 0

    x += 1
cv2.imwrite('navar.jpg',img)

cv2.imshow("img", img)
cv2.waitKey()