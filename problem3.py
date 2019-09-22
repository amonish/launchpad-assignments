a=[1,2,3,2,0,65,21,4,2,10]
print(a)
b=[]
for i in range(len(a)):
    if a[i]==2:
        b.append(i)

list(b)