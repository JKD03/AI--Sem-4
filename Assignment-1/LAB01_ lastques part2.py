# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:12:12 2022

@author: jkd
"""

from LAB01 import function

prin,rate,time=map(float,input("enter principal amount,rate of interest and time =>").split())

print("The compound interest is ",function(prin,rate,time))