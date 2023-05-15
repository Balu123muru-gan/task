                #pattern method 
##n= int (input("Enter:"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end="")
##    print()
#--------------------------------------------->
##n= int (input("Enter:"))
##for i in range(n,0,-1):
##    for j in range(1,i+1):
##        print(j,end="")
##    print()

#---------------------------------------------->
##n= int (input("Enter:"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print("{0}{0}".format(j,i),end=" ")
##        #print("{0}{1}".format(j,i),end=" ")
##    print()
#--------------------------------------------------->
##ch=65
##n= int (input("Enter:"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(chr(ch+j),end="")
##        #print("{0}".format(chr(ch+1)),end=" ")
##    print()

#--------------------------------------------------------->
##ch=65
##n= int (input("Enter:"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        ch=ch+1
##        #print(chr(ch+j),end="")
##        print("{0}".format(chr(ch)),end=" ")
##    print()
##    
##
##for i in range(n-1,0,-1):
##    for j in range(1,i+1):
##        ch=ch+1
##        print(chr(ch),end=" ")
##        #print("{0}".format(chr(ch+1)),end=" ")
##    print()
#-------------------------------------------------------------->
##sum=0
##n= int (input("Enter:"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        sum=sum+1
##        #print(sum,end=" ")
##        print("{:02d}".format(sum),end=" ")
##    print()
#---------------------------------------------->
##n= int (input("Enter:"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print("{0}{0}".format(j,i),end=" ")
##        #print("{0}{1}".format(j,i),end=" ")
##    print()
#------------------------------------------------------->
##n= int (input("Enter:"))
##for i in range(n):
##    for j in range(n-i-1):
##        print("0",end="")
##    for j in range(i+1):
##        print("*",end="")
##    print()

n= int (input("Enter:"))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i,0,-1):
        print(j+1,end="")
    print()
