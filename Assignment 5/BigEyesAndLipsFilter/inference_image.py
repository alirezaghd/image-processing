import numpy as np
import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

# Initialize face detector and face alignment models
face_detector = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
landmark_detector = CoordinateAlignmentModel("weights/coor_2d106.tflite")

# Read the input image
input_image = cv2.imread("a.jpg")
detected_boxes, _ = face_detector.inference(input_image)

# Zoom factor
zoom_factor = 2  

def apply_zoom(image, landmark_points):
    for landmarks in landmark_detector.get_landmarks(image, detected_boxes):  

        landmarks_selected = [landmarks[i] for i in landmark_points]
        landmarks_selected = np.array(landmarks_selected, dtype=int)  

        x, y, w, h = cv2.boundingRect(landmarks_selected)  
        mask = np.zeros_like(image, dtype=np.uint8)  
        cv2.drawContours(mask, [landmarks_selected], -1, (255, 255, 255), -1)  

        mask = mask // 255

        masked_image = image * mask   
        masked_image = masked_image[y:y+h, x:x+w]  
        mask = mask[y:y+h, x:x+w]    
       
        resized_masked_image = cv2.resize(masked_image, (0, 0), fx=zoom_factor, fy=zoom_factor)
        resized_mask = cv2.resize(mask, (0, 0), fx=zoom_factor, fy=zoom_factor)  

        final_masked_image = np.zeros(image.shape, dtype=np.uint8)
        final_mask = np.zeros(image.shape, dtype=np.uint8)

        x = x - (w//2)
        y = y - (h//2)

        final_masked_image[y:y+h*2, x:x+w*2] = resized_masked_image
        final_mask[y:y+h*2, x:x+w*2] = resized_mask

        result = final_masked_image + image *(1 - final_mask)

        return result
    
    


lip_landmarks = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
left_eye_landmarks  = [39, 37, 33, 36, 35, 41, 40, 42]
right_eye_landmarks = [95, 94, 96, 93, 91, 87, 90, 89]

result_image = apply_zoom(input_image, lip_landmarks)             
result_image = apply_zoom(result_image, left_eye_landmarks)             
result_image = apply_zoom(result_image, right_eye_landmarks)             
                
cv2.imshow("Result", result_image)
cv2.imwrite("output/result_face.jpg", result_image)
cv2.waitKey()
