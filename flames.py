name1=list(input().upper())
name2=list(input().upper())
len1=len(name1)
len2=len(name2)


for i in range(len1):
    for j in range(len2):
        if name1[i]==name2[j]:
            name1[i]='-'
            name2[j]='-'
      
print(name1)
print(name2)
name1=" ".join(name1)
name2=" ".join(name2)
print(name1)
print(name2)
tot=len(name1)+len(name2)
print(tot)
for k in range(tot%2==0):
    print(k)
