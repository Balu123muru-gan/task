                               #pattern
#1)
##n=int(input())
##for i in range(n):
##    for j in range(i+1):
##        print(i,end="")
##    print()
    
#------------------------------------------------------------>

#2)
##n=int(input())
##for i in range(n):
##    for j in range(i+1):
##        print(j+1,end="")
##    print()
#--------------------------------------------------------->


####3)
##n=int(input())
##for i in range(n):
##    for j in range(n,i-1,-1):
##        print(j,end="") 
##    print()
#------------------------------------------------------------------->

##4)
##n=int(input())
##for i in range(n,0,-1):
##    for j in range(i-1):
##        print(n,end="")
##    print()
#-------------------------------------------------------------->
#5
##n=int(input())
##for i in range(n,0,-1):
##    for j in range(i-0):
##        print(i,end="")
##    print()

#---------------------------------------------------------->
#6
##n=int(input())
##for i in range(n):
##    for j in range(n-i):
##        print(j,end="")
##    print()
#--------------------------------------------------->
#7
##n=int(input())
##for i in range(1,n):
##    for j in range(i,0,-1):
##        print(j,end="")
##    print()
#------------------------------------------------------->
#8
##n=int(input())
##for i in range(1,n):
##    for j in range(-1+i,-1,-1):
##        print(2**j,end="")
##    print()
#---------------------------------------------------->
#9
##n=int(input())
##for i in range(1,n):
##    for j in range(0,i,2):
##        print(2**i,end="")
##    print()
#--------------------------------------------------->
#10
##k=1
##n=int(input())
##for i in range(n):
##    
##    for j in range(i,0,-2):
##        print(k,end="")
##        
##        k+=1
##    print()
#================================================>
##n=int(input("enter;"))
##for k in range(1,n+1):
##    t=k
##    a=str(t)
##    b=list(a)
##    print(b)
##    count=1
##    A=[]
##    for i in b:
##        #print(i)
##        c=int(i)
##        A.append(c)
##        if c not in A:
##            A.append(c)
##        else:
##            A.append(c)
##    sum=0
##    if count>=2:
##        for r in range(len(A)):
##            sum=sum+A[r]
##        if sum<=5:
##            print(t)
#===================================>
##name1,name2,name3=input("enter 3 names:").split()
##print("name1:",name1)
##print("name2:",name2)
##print("name3:",name3)

##para=["23","22","33"]
##print("|".join(para))


#---------------------------------------------------------------->

##n= int (input("Enter:"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end="")
##    print()
##
##n= int (input("Enter:"))
##for i in range(n,0,-1):
##    for j in range(1,i+1):
##        print(j,end="")
##    print()


n= int (input("Enter:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("{0}{1}".format(j,i),end=" ")
    print()
##
##m=[1,2,3,4,5,6,7,8]
##for i in m:
##    print(i)

