import cv2

img = cv2.imread("4.jpg",0)

height, width = img.shape
print(img.shape)
for i in range(height):
    for j in range(width):
        if img[i,j] < 195 :
            img[i,j] = 0

cv2.imshow("img",img)
cv2.waitKey()
