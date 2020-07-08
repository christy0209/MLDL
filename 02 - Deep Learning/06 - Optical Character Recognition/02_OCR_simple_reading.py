# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:26:53 2020

@author: chris
"""

import cv2
import numpy as np

img = cv2.imread('data/novel.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)




# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


gray = get_grayscale(img)
noise = remove_noise(gray)



import matplotlib.pyplot as plt

plt.subplot(221); plt.title("gray"); plt.imshow(gray, cmap='gray');
plt.subplot(222); plt.title("noise"); plt.imshow(noise);



plt.show()

import pytesseract

img = gray
print("gray ocr")
print(pytesseract.image_to_string(img))

img = noise
print("\n\nnoise reoved ocr")
print(pytesseract.image_to_string(img))



