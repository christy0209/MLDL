# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:36:30 2020

@author: chris
"""
import pytesseract
import cv2
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('data/90degree.png')
osd = pytesseract.image_to_osd(img)
osd = osd.split("\n")
osd_dict = dict()
for x in osd:
    osd_dict[x.split(":")[0]] = x.split(":")[1]
print(osd_dict)