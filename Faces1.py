import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread("lidi.jpg")
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.circle(img, (x+round(w/2), y+round(h/2)), round(w/2), (255, 0, 0), -1)
    cv2.circle(img, (x+round(w/2)-12, y+round(h/2)-12), 5, (255, 70, 0), -1)
    cv2.circle(img, (x+round(w/2)+12, y+round(h/2)-12), 5, (255, 70, 0), -1)
    cv2.line(img, (x+round(w/2)+12, y+round(h/2)+12), (x+round(w/2), y+round(h/2)+16), (255, 70, 0), 5)
    cv2.line(img, (x+round(w/2), y+round(h/2)+16), (x+round(w/2)-12, y+round(h/2)+12), (255, 70, 0), 5)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
