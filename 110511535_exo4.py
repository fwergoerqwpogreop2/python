# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:31:14 2019

@author: User
"""

month = int(input("請輸入月份："))
if month >= 3 and month <= 5:
    print(str(month)+"月是春天")
elif month >= 6 and month <= 8:
     print(str(month)+"月是夏天")
elif month >= 9 and month <= 11:
     print(str(month)+"月是秋天")
elif month ==12 or month == 1 or month == 2 :
     print(str(month)+"月是冬天")
else:
    print("你不知道一年有幾月嗎?")