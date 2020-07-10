# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:41:54 2020

@author: chris
"""

import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('data/sample2.jpg')
custom_config = r'--oem 3 --psm 6 outputbase digits'
print(pytesseract.image_to_string(img, config=custom_config))


#whitelisting
custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
print("\nWhitelisted")
print(pytesseract.image_to_string(img, config=custom_config))

#blacklisting
custom_config = r'-c tessedit_char_blacklist=0123456789 --psm 6'
print("\nBlacklisted")
print(pytesseract.image_to_string(img, config=custom_config))