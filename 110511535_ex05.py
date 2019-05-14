# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:37:23 2019

@author: User
"""

a = int(input("請輸入今年收入淨額："))
print("付稅金額：",end="")
if(a >= 2000000):
    print(a*0.3, end=" 元\n")  
elif(a >= 1000000):
    print(a*0.21, end=" 元\n")
elif(a >= 600000):
    print(a * 0.13, end=" 元\n") 
elif(a >= 300000):
    print(a * 0.06, end=" 元\n") 
else:
    print(a *0, end=" 元\n")