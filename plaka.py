# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:05:52 2024

@author: Berkay
"""
import cv2
import pytesseract
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
resim=cv2.imread("7327.jpg")
plt.axis("off")
plt.title("plaka Afyon")
plt.imshow(resim)
metin=pytesseract.image_to_string(resim)
print(metin)

