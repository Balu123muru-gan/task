n="balu","poovarasan","malini","gowtham","santhosh"
k=list(n)
lk=len(k)
#print(k)
sum=0
for i in range(len(k)):
    for j in range(i+1,len(k)):
        #sum=sum+k[i]
        
        if k[i]<k[j]:
            temp=k[i]
            k[i]=k[j]   
            k[j]=temp
print(k)
