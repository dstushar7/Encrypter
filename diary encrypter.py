m = str(input())
m = m.upper()
n = list(map(ord,m))
for item in n:
    temp = item + 25
    item = item + (25 - (temp - 90)*2)
    print(chr(item))
