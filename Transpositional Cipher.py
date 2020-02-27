# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""
import numpy as np
msg = str(input("Enter your message: "))
msg = msg.replace(" ","") #removing white spaces
msg = msg.lower() #converting to all lower case
l = len(msg)
m = int(l/6)
n = l%6
for i in range(0,6-n):
    msg = msg+'a'
msg = list(msg) #convereting to list
matrix = np.array(msg).reshape(m+1,6)
#Converting list to a numpy matrix