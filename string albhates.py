#n="balamurugan"

"""
k=[]
for i in n:
     k.append(i)
     print(i)
k=list(n)"""
"""print(k)
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if k[i]>k[j]:
            temp=k[i]
            k[i]=k[j]
            k[j]=temp
print(k)
ans=''.join(k)
print(ans)"""



n=["bala","murugan","gowtham","malini","poovarasan","sakthi"]
ans=[]

"""
k=[]
for i in n:
     k.append(i)
     print(i)"""
for s in n:
    k=list(s)
    #print(k)
    for i in range(len(k)):
        for j in range(i+1,len(k)):
            if k[i]>k[j]:
                temp=k[i]
                k[i]=k[j]
                k[j]=temp
    #print(k)
    ans.append(" ".join(k))
    print(ans)


