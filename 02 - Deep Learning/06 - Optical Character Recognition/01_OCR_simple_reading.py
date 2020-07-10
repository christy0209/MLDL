# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:15:26 2020

@author: chris
"""
#download tesseract - https://github.com/UB-Mannheim/tesseract/wiki - for windows
#https://tesseract-ocr.github.io/tessdoc/Home.html -for linux
#install pytesseract - pip install pytesseract

import time

import cv2
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('data/novel.png') #reading image
start = time.time()
print("Text extracted using Tesseract\n")
print(pytesseract.image_to_string(img))
end = time.time()
t = end-start
print("\nTime Taken   ", t, " (s)")