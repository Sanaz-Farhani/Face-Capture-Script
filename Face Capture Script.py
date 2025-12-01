import cv2
import cv2.data
import os 
cap = cv2.VideoCapture(0)

name_of_img = input("whats your name?")
full_path = f"D:/face/{name_of_img}.jpg"
while True :
    ret , frame = cap.read()
    
    if not ret:
        break


    img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
    face = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors= 5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame , (x,y) , (x+w , y+h)  ,(255,0,0) , 5)
        cropped_img = frame[y:y+h, x:x+w]
    key = key = cv2.waitKey(1) & 0xFF

    cv2.imshow("LIVE VIDEO", frame)
    if key == ord("s"):
        cv2.imwrite(full_path, cropped_img)
        print ("Saved")
    elif key == ord("q") :
        break


cap.release()
cv2.destroyAllWindows()