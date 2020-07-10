# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:39:43 2020

@author: chris
"""

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('data/text.png')

base_coor = [70, 45, 300, 85]

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    ix=int(b[1])
    iy=h-int(b[2])
    x = int(b[3])
    y = h-int(b[4])
    
    if(ix >base_coor[0] and x < base_coor[2] and iy > base_coor[1] and y < base_coor[3]):
        print(ix,iy,x,y)
        #img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 1)
        img = cv2.rectangle(img, (ix, iy), (x,y), (0, 255, 0), 1)

# cv2.imshow('img', img)
# cv2.waitKey(0)

import matplotlib.pyplot as plt

plt.imshow(img)
plt.title("Bounding Boxes")
plt.show()
cv2.imwrite("data/op/hdfc_bouding_box.jpg",img)

