import cv2

image = cv2.imread("Batman/bat.jpg")
print(image.shape)
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
font = cv2.FONT_HERSHEY_COMPLEX
_,image = cv2.threshold(image,140,255,cv2.THRESH_BINARY_INV)

image = cv2.putText(image,"BATMAN",(430,480),font,1,249,2,3)
cv2.imshow("Result",image)
cv2.imwrite("Result.jpg",image)
cv2.waitKey()