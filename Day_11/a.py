a=[10, 7, 7, 7]
b = 0
for i in a:
    b = b + i
    if 7 in a and b > 30:
        a.remove(7)
        a.append(21)
print(a)
if 7 in a and b > 30:
    a.remove(7)
    a.append(21)
print(a)