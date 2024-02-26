import cv2
import numpy as np

room_background = cv2.imread("Virtual decoration/Input/room_background.jpg", 0)
room_foreground = cv2.imread("Virtual decoration/Input/room_foreground.jpg", 0)
room_mask = cv2.imread("Virtual decoration/Input/room_mask.jpg", 0)



room_background = room_background.astype(np.float32)
room_foreground = room_foreground.astype(np.float32)
room_mask = room_mask.astype(np.float32)

normalized_mask = room_mask / 255.0
result_foreground_masked = cv2.multiply(room_foreground, normalized_mask)

mask_inverted = 255 - room_mask
normalized_mask_inverted = mask_inverted / 255.0
result_background_masked = cv2.multiply(room_background, normalized_mask_inverted)

result = cv2.add(result_foreground_masked, result_background_masked)
result = result.astype(np.uint8)


cv2.namedWindow("result", cv2.WINDOW_NORMAL) 
cv2.imshow("result", result)
cv2.imwrite("Virtual decoration/Output/result.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
