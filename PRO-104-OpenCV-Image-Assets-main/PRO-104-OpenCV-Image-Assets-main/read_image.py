import cv2
img = cv2.imread("butterfly.jpg")
cv2.imshow("Display Image", img)


gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Grayscale", gray_image)
cv2.waitkey(0)
