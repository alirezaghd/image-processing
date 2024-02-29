import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
import sys
from TFLiteFaceAlignment import CoordinateAlignmentModel


fd = UltraLightFaceDetecion("weights/RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

# cap = cv2.VideoCapture(0)
image = cv2.imread("a.jpg")
color = (0, 0, 255)

start_time = time.perf_counter()

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes): # تعداد افراد
    # for i , p in enumerate(np.round(pred).astype(np.uint)): # به تعداد دایره ها تکرار میشه
    #     cv2.circle(image, tuple(p), 1, color, 1, cv2.LINE_AA)
    #     cv2.putText(image, str(i),tuple(p),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    
    lips_landmark = []
    for i in [52,55,56,53,59,58,61,68,67,71,63,64]:
        lips_landmark.append(pred[i])
    lips_landmark = np.array(lips_landmark, dtype=int)
    print(lips_landmark)
x, y, w, h = cv2.boundingRect(lips_landmark)
mask = np.zeros(image.shape, dtype=np.uint8)
cv2.drawContours(mask,[lips_landmark],-1,(255,255,255),-1)

mask = mask // 255
result = image * mask

result = result[y:y+h, x:x+w]

result_big = cv2.resize(result,(0,0),fx=2 , fy=2)

print(time.perf_counter() - start_time)

cv2.imshow("result", result_big)
cv2.waitKey()
cv2.imwrite("output/result.jpg", result_big)