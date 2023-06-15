import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread("lidi.jpg")
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw circle around the faces

center = (450, 325)
radius = 200
color = (0, 255, 255)

for (x, y, w, h) in faces:
    cv2.circle(img, center, radius, color, -1)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
