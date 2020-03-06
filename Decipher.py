# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 04:50:17 2020

@author: dstus
"""

import numpy as np
enk = str(input("Enter Encryption Key with no repeated letters: " ))
cip = str(input("Enter Cipher Text: "))
lenk= len(enk)
lenc= len(cip)
enk = ctos(enk)
cip = ctos(cip)
m   = int(lenc/lenk)
cip = list(cip)
enk = list(enk)
a = set(enk)
if len(a) == len(enk):
    matrix = np.array(cip).reshape(lenk,m)
    ensort = enk.copy()
    ensort.sort()
    mapp = dict()
    for i in range(lenk):
        mapp[ensort[i]] = matrix[i] #set columns as key's letter
    a = []
    for i in enk:
        a.append(mapp[i])
    matrix = np.array(a)
    matrix = matrix.T
    a = []
    for i in range(m):
        for j in range(lenk):
            a.append(matrix[i][j]) #take the cipher text list as output
    c = ''.join(str(e) for e in a) #convert to string
    print(c)
else:
    print('ERROR!!! Your key got repeated letters in it')