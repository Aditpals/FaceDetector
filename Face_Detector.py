import cv2
from random import randrange

#Loading pre-trained data.
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

"""#Selecting an image to detect face
#img = cv2.imread('RDJ.jpg')


#Turn image to gray-scale
grayScaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayScaled_img)

#Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(255),randrange(255),randrange(255)), 2)
    
#Show the selected image
cv2.imshow("Face Detector", img)

#Wait for press key to close
cv2.waitKey()
"""""
#Video capture

webcam= cv2.VideoCapture(0)

#Iterate forever over frames

while True:
    successful_frame_read, frame=webcam.read()
    grayScaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayScaled_img)
    #Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)
     
    cv2.imshow("Face Detector", frame)
    key=cv2.waitKey(1)
    
    if key ==81 or key ==113:
        break
    



