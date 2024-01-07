#listoperations

l=[1,2,4,5,6,67,7]
for i in l:
    print(i)
print(type(l))
print(len(l))
l[0]=5
print(l)
l.append(6)
print(l)
l.append(9)
print(l)
l.insert(1,10)
print(l)
l.remove(10)
print(l)
l.pop()
print(l)
l.pop(1)
print(l)
l.pop(2)
print(l)

a=[1,2,3,4]
b=[5,6,7,8]
a.extend(b)
print(a)
print(b)
