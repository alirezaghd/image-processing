import cv2
import numpy as np

image = cv2.imread("PhotoToSketch/Input/a.jpg",0)


inverted = 255 - image
blurred = cv2. GaussianBlur(inverted, (21, 21), 0)
inverted_blurred = 255 - blurred

sketch = image / inverted_blurred

result  = cv2.multiply(sketch,255)


cv2.namedWindow("result", cv2.WINDOW_NORMAL)
cv2.imshow("result", result)
cv2.imwrite("PhotoToSketch/Output/result1.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
