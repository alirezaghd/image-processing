import cv2
import numpy as np

# Load the images
image1 = cv2.imread("FaceMorphing/Input/Biden.jpg")
image2 = cv2.imread("FaceMorphing/Input/Trump.jpg")


cv2.namedWindow("out", cv2.WINDOW_NORMAL) 
# cv2.imshow("out", final_image)
cv2.waitKey()
cv2.destroyAllWindows()
