# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:41:02 2020

@author: chris
"""

import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('data/rating_Cards/ronaldo.png')
#base_coor = [48, 2, 327, 31]

default_shape = (593, 447, 3)

base_coor =  [60, 320, 391, 368] #x1,y1,x2,y2
d = pytesseract.image_to_data(img, output_type=Output.DICT)
#print(d.keys())

data = ""

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > -2:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        x1=x
        y1=y
        x2= x+w  #x2 is equal to x1+width
        y2= y+h  #y2 is equal to y1+height
        
        if (x1>=base_coor[0] and x2 <= base_coor[2] and y1>=base_coor[1] and y2 <= base_coor[3]):
            #print(x, y, x+w, y+h)
            img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            data= data+" "+d['text'][i]


import matplotlib.pyplot as plt

plt.imshow(img)
plt.title("Bounding Boxes With Dictionary")
plt.show()
cv2.imwrite("dbs_boudning_box.jpg",img)
print(data)