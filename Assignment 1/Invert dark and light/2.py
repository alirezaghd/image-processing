import cv2


img1 = cv2.imread('/Alpha/1.jpg',0)
img2 = cv2.imread('/Alpha/2.jpg',0)

height, width = img1.shape

img1 *= 255
img2 *= 255
cv2.imwrite('img1.jpg',img1)
cv2.imwrite('img2.jpg',img2)
cv2.imshow('img1',img1) 
cv2.imshow('img2',img2) 
cv2.waitKey()