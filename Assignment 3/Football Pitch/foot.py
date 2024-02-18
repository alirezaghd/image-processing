import cv2
import numpy as np

width = 800
height = 600
array = np.zeros((height, width, 3), dtype=np.uint8)

rect_width = 100

for i in range(0, width, rect_width):
    for j in range(height):

        color = [66,125,17] if i // rect_width % 2 == 0 else [71,139,16]

        array[:, i:i+rect_width] = color


cv2.line(array, (width // 2, 0), (width // 2, height), (255, 255, 255), 5)

cv2.rectangle(array, (50, 50), (width - 50, height - 50), (255, 255, 255), 5)


corner_points = [(50, 50), (width - 50, 50), (50, height - 50), (width - 50, height - 50)]
for point in corner_points:
    cv2.circle(array, point, 10, (255, 255, 255), -1)


goal_width = 100
goal_height = 200
goal_y = (height - goal_height) // 2
left_goal_x = 50
right_goal_x = 650
cv2.rectangle(array, (left_goal_x, goal_y), (left_goal_x + goal_width, goal_y + goal_height), (255, 255, 255), 5)
cv2.rectangle(array, (right_goal_x, goal_y), (right_goal_x + goal_width, goal_y + goal_height), (255, 255, 255), 5)


center_circle_radius = 80
center_circle_center = (width // 2, height // 2)
cv2.circle(array, center_circle_center, center_circle_radius, (255, 255, 255), 5)


cv2.imshow('Photo', array) 
cv2.waitKey()
