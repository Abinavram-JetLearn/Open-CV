import cv2
import os
img = cv2.imread("4. Open CV with Python\lesson 2\Bilateral.jpg")
import numpy 
# cv2.imshow("screen", img)
# cv2.waitKey(0)
# b,g,r = cv2.split(img)
# cv2.imshow("blue", b)
# cv2.waitKey(5000)
# cv2.imshow("green", g)
# cv2.waitKey(5000)
# cv2.imshow("red", r)
# cv2.waitKey(5000)

# Arithmatic Operation on Images
# diamond = cv2.imread("4. Open CV with Python\lesson 2\diamond addition.jpeg")
# star = cv2.imread("4. Open CV with Python\lesson 2\star addition.jpeg")
# add = cv2.addWeighted(star, 0.4, diamond, 0.6, 1)
# cv2.imshow("added", add)
# cv2.waitKey(5000)
# subtract = cv2.subtract(star, diamond)
# cv2.imshow("Subtracted", subtract)
# cv2.waitKey(5000)

pikachu = cv2.imread("4. Open CV with Python\lesson 2\pika.png")
respika = cv2.resize(pikachu, (100,100))
cv2.imwrite("respika.png", respika)
kernel = numpy.ones((1,1), numpy.uint8)
erode = cv2.erode(pikachu, kernel)
cv2.imshow("Erode", erode)
cv2.waitKey(5000)