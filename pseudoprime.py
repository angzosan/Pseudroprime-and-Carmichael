# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:50:50 2021
@author: user
"""

def pseudoprime(base,m):
    if ((base**(m-1)-1)%m==0):
          return True
    return False

m=3914864773
base=2
x=pseudoprime(base,m)
if (x):
    print(m," is a pseudoprime")
else:
    print(m," is not a pseudoprime")
