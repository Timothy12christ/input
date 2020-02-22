# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:23:31 2019

@author: ASUS
"""

products=[]
while True:
    box=input('請輸入東西')
    if box=='q':
        break
    products.append(box)
print(products)