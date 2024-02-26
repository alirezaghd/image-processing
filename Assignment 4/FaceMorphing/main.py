import cv2
import numpy as np

image1 = cv2.imread("FaceMorphing/Input/Biden.jpg")
image2 = cv2.imread("FaceMorphing/Input/Trump.jpg")

# 
result1 = cv2.add(cv2.multiply(image1, 3/4), cv2.multiply(image2, 1/4))
result2 = cv2.add(cv2.multiply(image1, 2/4), cv2.multiply(image2, 2/4))
result3 = cv2.add(cv2.multiply(image1, 1/4), cv2.multiply(image2, 3/4))

concatenated_image = np.concatenate((image1, result1, result2, result3, image2), axis=1)

# Display the result
cv2.namedWindow("out", cv2.WINDOW_NORMAL)
cv2.imshow("out", concatenated_image)
cv2.imwrite("FaceMorphing/Output/result.jpg", concatenated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
