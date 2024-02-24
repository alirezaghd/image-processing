import cv2
import numpy as np

# Load the two images
image1 = cv2.imread("FaceMorphing/Input/Biden.jpg")
image2 = cv2.imread("FaceMorphing/Input/Trump.jpg")

# Concatenate the two images horizontally
concatenated_image = np.concatenate((image1, image2), axis=1)

# Display the concatenated image
cv2.namedWindow("out", cv2.WINDOW_NORMAL) 
cv2.imshow("out", concatenated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
