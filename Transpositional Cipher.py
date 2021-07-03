def ctos(x):#convert to required structure
    x = x.replace(" ","")#remove white spaces
    x = x.lower()#convert to lowercase
    return x

import numpy as np
enk = str(input("Enter Encryption Key with no repeated letters: "))
msg = str(input("Enter your message: "))
enk = ctos(enk)
msg = ctos(msg)
lenk = len(enk)
lenm = len(msg)
m = int(lenm/lenk)#To know the number of rows
n = lenm%lenk
for i in range(lenk-n):
    msg = msg+'a'
msg = list(msg)
enk = list(enk)
matrix = np.array(msg).reshape(m+1,lenk) #making the matrix of the message
matrix = matrix.T #Transpose the matrix to point the indexes to a dictionary's key
keyd = dict()
for i in range(lenk):
    keyd[enk[i]] = matrix[i] #set columns as key's letter
enk.sort() #sorting the key
a = []
for i in enk:
    a.append(keyd[i]) #taking the sorted columns along with dictionary values
matrix = np.array(a) #taking numpy matrix to easily access
a = []
for i in range(lenk):
    for j in range(m+1):
        a.append(matrix[i][j]) #take the cipher text list as output
c = ''.join(str(e) for e in a) #convert to string
print(c)