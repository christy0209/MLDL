# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:39:43 2020

@author: chris
"""

import cv2
import pytesseract

img = cv2.imread('data/sample1.jpg')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)

import matplotlib.pyplot as plt

plt.imshow(img)
plt.title("Bounding Boxes")
plt.show()
