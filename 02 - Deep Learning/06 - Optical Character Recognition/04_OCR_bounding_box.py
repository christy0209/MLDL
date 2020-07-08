# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:41:02 2020

@author: chris
"""

import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('data/invoice.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


import matplotlib.pyplot as plt

plt.imshow(img)
plt.title("Bounding Boxes With Dictionary")
plt.show()
cv2.imwrite("boudning_box.jpg",img)