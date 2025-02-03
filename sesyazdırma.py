# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:06:33 2024

@author: Berkay
"""
# import time
# sistem_zamani=time.asctime()

# import speech_recognition as sr

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Sesiniz kaydediliyor...")
#     ses = r.listen(source, phrase_time_limit=5)
#     try:
#         text=(r.recognize_google(ses, language="tr-TR"))    
#     except sr.UnknownValueError:
#         text=("Sesiniz anlaşılmıyor.")
#     except sr.RequestError:
#         text=("Bağlantınızı kontrol ediniz.")
#     #a yazdırmaya devam eder, w ise dosyanın üstüne yazar
#     f=open("kayit.txt","a")
#     f.write("\n" + text + " " sistem_zamani)
#     f.close()

import os
from gtts import gTTS

language = "tr"
text = "Biribirdir"
output=gTTS(text, lang=language) 
output.save("output.mp3")
os.system("start output.mp3")