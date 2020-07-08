# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:15:26 2020

@author: chris
"""
#download tesseract - https://github.com/UB-Mannheim/tesseract/wiki
import time

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('data/novel.png')
start = time.time()
print(pytesseract.image_to_string(img))
end = time.time()
print("Time Taken   ", end-start, " (s)")