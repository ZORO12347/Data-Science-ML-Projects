import numpy as np
import cv2

img = np.zeros((800, 800, 3), dtype = np.uint8)

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            img [i * 100 : (i+1) * 100, j * 100 : (j + 1) * 100] = 255, 255, 255

cv2.imshow('Checkerboard', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
