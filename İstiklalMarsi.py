# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:35:52 2024

@author: Berkay
"""
import cv2
import pytesseract
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
resim=cv2.imread(r"istiklal.jpg")
plt.axis("off")
plt.imshow(resim)
metin=pytesseract.image_to_string(resim)
print(metin)
import os
from gtts import gTTS
language = "tr"
text = metin
output=gTTS(text, lang=language) 
output.save("istiklalmarsi.mp3")
os.system("start istiklalmarsi.mp3")