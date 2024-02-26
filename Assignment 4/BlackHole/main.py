import cv2 
import numpy as np
import os

images = []

for i in range(1, 5):
    images_path = os.listdir("BlackHole/Input/black_hole/" + str(i))
    for image_path in images_path:
        image = cv2.imread("BlackHole/Input/black_hole/" + str(i) + "/" + image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = image.astype(np.float32)
        images.append(image)

image_without_noise = []

for i in range(4):
    image_sum = np.zeros_like(images[0], dtype=np.float32)
    for j in range(5):
        image_sum += images[i * 5 + j]
    image_without_noise.append(image_sum / 5)

final_image = np.zeros((2000, 2000), dtype=np.uint8)

final_image[0:1000, 0:1000] = image_without_noise[0]
final_image[0:1000, 1000:2000] = image_without_noise[1]
final_image[1000:2000, 0:1000] = image_without_noise[2]
final_image[1000:2000, 1000:2000] = image_without_noise[3]

cv2.imwrite("BlackHole/Output/result.jpg", final_image)
cv2.imshow('result', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
