##a=input()
##b=a[::-1]
##b= reversed(a)
##print(b)
##str=" "
##for i in a:
##    str=i+str
##print(str)
##    
n=["bala","murugan","poovarasan","gowtham","malini"]
ans=[ ]
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
print(ans,sep=" ")




 
