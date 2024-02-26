import cv2
import numpy as np
image1 = cv2.imread("secret text/Input/a.png",0)
image2 = cv2.imread("secret text/Input/b.png",0)


image1 = image1.astype(np.float32)
image1 = image1 / 255
image2 = image2.astype(np.float32)
image2 = image2 / 255

result = cv2.subtract(image1,image2)
result = result.astype(np.uint8)

cv2.namedWindow("out", cv2.WINDOW_NORMAL) 
cv2.imshow("out", result)
cv2.imwrite("secret text/Output/result.jpg", result)
cv2.waitKey()
cv2.destroyAllWindows()
