import cv2  
  
# Load the cascade  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
  
# To capture video from webcam.   
cam_port = 0
cam = cv2.VideoCapture(cam_port)
  
# reading the input using the camera
result, img = cam.read()
  
    # Convert to grayscale  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
    # Detect the faces  
faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
  
    # Draw the rectangle around each face  
for (x, y, w, h) in faces:  
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
  
    # Display  
cv2.imshow('Video', img)  
  
    # Stop if escape key is pressed  
k = cv2.waitKey(30) & 0xff  
 
          
# Release the VideoCapture object  
cam.release()  