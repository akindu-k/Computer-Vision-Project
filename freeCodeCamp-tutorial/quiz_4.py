import cv2
import numpy as np
import matplotlib.pyplot as plt

a = [[1,1,1],[1,0,0],[0,0,0]]
b = [[1,1,0],[1,1,0],[1,0,0]]

out = cv2.bitwise_and(a,b)
plt.imshow(out)