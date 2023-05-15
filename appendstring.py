def show(a,b,i):
    return a[:i]+b+a[i:]

a=input("Enter string:")
b=input("Enter mid string:")
i=int(input("Enter index:"))
print(show(a,b,i))

#-----------------------------

a="balagan"
c=list(a)
print(c)
index=int(input("Enter index:"))
st=input("Enter mid name:")
length=len(st)
for i in range(0,length):
    c.insert(i+index,a[i])
ans="".join(c)
print(ans)
