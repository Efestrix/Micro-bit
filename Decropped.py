import cv2

imgs = []

for i in range(210):
    img = cv2.imread("cropped1/c_{i}.jpg".format(i=i))
    imgs.append(img)

final = cv2.hconcat(imgs)

cv2.imshow("final", final)

cv2.waitKey()
cv2.destroyAllWindows()
