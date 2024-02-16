import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    height, width = frame.shape

    center_x = int(width / 2)
    center_y = int(height / 2)
    
    rec = cv2.rectangle(frame,(center_x - 50, center_y - 50), (center_x + 50, center_y + 50),200,3)
    x,y = rec.shape
    box_checker = frame[190:290,270:370]

    blurred_frame = cv2.blur(frame, (20, 20), 0)
    blurred_frame[190:290,270:370] = box_checker 
    text = None
     
    for r in range(290,350):
        for c in range(210,270):
            if blurred_frame[r, c] > 150:
                text = "White"
                #break
            elif blurred_frame[r, c] < 50:
                text = "Black"
                #break
            elif 50 <= blurred_frame[r, c] <= 150:
                text = "Gray"
                #break

    cv2.putText(blurred_frame, text, (20, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
    

    cv2.imshow("out", blurred_frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
