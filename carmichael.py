# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:34:27 2021
@author: user
"""
import math

def carmichael(num,m):
    if ((num**(m-1)-1)%m==0):
          return True
    return False


p=8911
#p=341
flag=True
for i in range(2,p):
    if math.gcd(i,p)==1:
        if (carmichael(i,p)==False):
            print("Not carmichael beacause of ",i)
            flag=False
            break
if(flag):
   print("Is Carmichael")       
