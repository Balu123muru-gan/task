"""m=int(input())
a=-1
b=1
for i in range(m):
    c=a+b
    print(c)
    a=b
    b=c"""

"""#fibonacci given range of value
x=int(input())
y=int(input())
m=-1
n=1
temp=[]
while(True):
    o=m+n  #o=0  
    if o>=x and o<=y:      # o>=5 and o<=40
        temp.append(o)
    m=n
    n=o
    if o>y:
        break
print(temp)"""

num=10
n1=55
n2=89
c=0
#for i in range(2,num):
while(True):
    n3=n1+n2
    n1=n2
    n2=n3
    if  n3%2==0:
        c=c+1
        print(n3,end=" ")
        if c==10:
            break
print()
#=============
num=10
n1=21
n2=34
c=0
#for i in range(2,num):
while(True):
    n3=n1+n2
    n1=n2
    n2=n3
    if  n3%2==1:
        c=c+1
        print(n3,end=" ")
        if c==10:
            break
print()
                        
    
