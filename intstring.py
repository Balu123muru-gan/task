'''n=[123,"a","b",456]
print(str(n))
a=[]
b=[]
for i in range(len(n)):
    if n[i]==int:
        a.append(n[i])
    else:
        b.append(n[i])
print(a)
print(b)
'''
n=['123asdf456','890lkjh789']
a=[]
b=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if(type(n[i]))==(type(n[j])):
            a.append(n[i])
        else:
            b.append(n[j])
print(a)
print(b)
