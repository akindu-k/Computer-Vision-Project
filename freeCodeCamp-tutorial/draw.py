import cv2 as cv
import numpy as np


blank = np.zeros((500,500), dtype="uint8")

img = cv.imread("Photos/ep1.png")
cv.imshow("Ep 1",img)
cv.waitKey(0)

