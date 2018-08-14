import cv2

import numpy as np

img = cv2.imread('icon.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
print(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img.item(i, j, 0) == 255 and img.item(i, j, 1) == 255 and img.item(i, j, 2) == 255:
            img.itemset((i, j, 3), 0)

cv2.imwrite('transicon.png', img)
