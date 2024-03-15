import cv2 

image = cv2.imread("a.jpg")

rotate = cv2.rotate(image,cv2.ROTATE_180)

cv2.imshow("result",rotate)
cv2.waitKey()