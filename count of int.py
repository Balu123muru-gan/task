n=[11,22,11,33,22,44,11,99,22,22,22,11,44,66,55,33,55,44]
b=set(n)
print(b)
a=list(b)
print(a)
for i in range(len(a)):
    count=0
    for  j in range(len(n)):
        if a[i]==n[j]:
            count+=1
    print("count %d:%d"%(a[i],count))


