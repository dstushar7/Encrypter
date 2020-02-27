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
    msg = msg+'a'#fill the matrix
msg = list(msg) #convereting to list
matrix = np.array(msg).reshape(m+1,6)
#Converting list to a numpy matrix
#positional matrix
a = []
for i in range(6):
    for j in range(m+1):
        a.append(matrix[j][i])
c = ''.join(str(e) for e in a)#converting list into string
print(c)
    