# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:22:50 2024

@author: Berkay
"""

import matplotlib.pyplot as plt

plt.title("baslik")
plt.xlabel("x eksemi başlığı")
plt.ylabel("y ekseni başlığı")
plt.axis([0,6,0,20])
plt.grid(True)
x=[1,2,3]
y=[4,5,6]
plt.plot(x,y,"-")
plt.show()