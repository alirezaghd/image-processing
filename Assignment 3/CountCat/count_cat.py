import cv2

image = cv2.imread("count cat\cats2.jpg")

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface_extended.xml")

faces = face_detector.detectMultiScale(image_gray,1.3)
count = 0
for face in faces:
    x,y,w,h = face
    cv2.rectangle(image_gray,(x,y),(x+w,y+h),0,4) 
    count += 1
    
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image_gray,f"number of cats : {count} ",(30,30),font,0.7,0,1)


cv2.imshow("out",image_gray)
cv2.imwrite("result.jpg",image_gray)
cv2.waitKey()