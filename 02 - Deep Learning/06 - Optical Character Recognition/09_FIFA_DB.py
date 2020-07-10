# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:37:47 2020

@author: chris
"""

import cv2
import os
import pandas as pd
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

axes = {
        "Name":[45, 425, 600, 570],
        "PAC":[135, 570, 205, 634],
        "SHO":[135, 634, 205, 684],
        "PAS":[135, 684, 205, 746],
        "DRI":[340, 570, 440, 634],
        "DEF":[340, 630, 440, 684],
        "PHY":[340, 684, 440, 746]
        }
ref_shape = (900, 644, 3)

def read_image(image):
    image = cv2.imread(image)
    return image
# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def resizing(image):
    dsize = (ref_shape[1],ref_shape[0])
    return cv2.resize(image, dsize)

def data_extraction(image):
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    n_boxes = len(d['text'])
    op_dict = dict()
    for key in axes:
        data = ""
        
        for i in range(n_boxes):
            if int(d['conf'][i]) > 70:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                x1=x
                y1=y
                x2= x+w  #x2 is equal to x1+width
                y2= y+h  #y2 is equal to y1+height
                if (x1>=axes[key][0]-10 and x2 <= axes[key][2]+10 and y1>=axes[key][1]-10 and y2 <= axes[key][3]+10):
                    data= data+" "+d['text'][i]
        op_dict[key]=data
    return(op_dict)
        
df = pd.DataFrame(columns=['Name','PAC','SHO','PAS','DRI','DEF','PHY'])
for x in os.listdir("data/cards"):           
    img = "C:\\Users\\chris\\Christy\\Luminar\\LuminarTechnoLab\\02 - Deep Learning\\06 - Optical Character Recognition\\data\\cards\\"+x
    image = read_image(img)
    resized = resizing(image)
    grey = get_grayscale(resized)
    op=data_extraction(grey)
    df =df.append(op, ignore_index=True)
df.to_csv("FIFA.csv",index=False)
    