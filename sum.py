'''k=[321,21,6314,94317,91]
var=1
for i in range(k):
    for j in range(i):
        var=k[i]%10*var
    
    
    
    print(var)'''

'''
n=[123,78]
ans=[]
rn=0
for s in n:
    print(s)
    #for i in range(s):
    #while s!=0:
    #if s>0:
    b=s%10
    print(b)
    s=s//10
    rn=rn*10+b
            
    print(rn)
    #ans.append(rn)
    #print(ans)
    #break
'''
a=[234,45,23]
x=[]
for i in a:
    s=0
    while(True):
        while i!=0:
            r=i%10
            i=i//10
            s=s+r
            print(s)
            if s<=9:
                x.append(s)
            print(x)
                break
            else:
                i=s
                s=0
print(x)


















        
            #print(b,end=" ")
'''
ans.append(str(b))
    print(ans)
    f=" ".join(ans)
    print(f)
'''            
    



a=[123,234]
#print(type(a))
s=0
x=[]
for i in a:
    for j in i:
        print(j)
'''        
    #print(i)
    while i!=0:
        r=i%10
        i=i//10
        s=s*10+r
    #print(s)
    x.append(s)
print(x)
        
'''   
'''
while a!=0:
   r=a%10
   a=a//10
   s=s*10+r
print(s)
'''







