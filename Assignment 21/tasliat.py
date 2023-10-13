import cv2

img=cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\blank.png",0)

j=0
for i in range(200):

  img[150-j:200-j,0+1*j:50+1*j]=0

  j=j+1

cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture4.jpg" ,img)
cv2.imshow('output',img)
cv2.waitKey()