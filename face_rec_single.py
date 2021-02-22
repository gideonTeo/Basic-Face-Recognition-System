import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

# img = cv2.imread('zhikai.JPG') # tester

while True:
    # read the frame
    _, img = cap.read()

    # convert the jpg image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect face
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # form bounding boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # display
    cv2.imshow('img', img)

    # if esc is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# release the video capture object
cap.release()
