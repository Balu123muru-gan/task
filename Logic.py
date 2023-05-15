#1)Reverse string

##m="balu"
####m=list(m)
####print(m)
##n=""
##for i in m:
##    n=i+n
##print(n)

#----------------------------------------------->
#REVERSE INT

##m=987
##n=0
##while m!=0:
##    r=m%10
##    n=n*10+r
##    m=m//10
##print(n)


##k=[123,456,789]
##for i in k:
##    m=i
##    n=0
##    while m!=0:
##        r=m%10
##        #print(m)
##        n=n*10+r
##        m=m//10
##    print(n)

##m=123
##m=str(m)
###print(m)
##n=""
##for i in m:
##    n=i+n
##print(n)

#slicing reverse
##num = 123456
##print(str(num)[::-1])

#
    
#----------------------------------------->
#2)fibonacci series
##n=int(input())
##a=-1
##b=1
##for i in range(n):
##    c=a+b
##    a=b
##    b=c
##    print(c)

#given range fibonacci series

##n=int(input())
##m=int(input())
##a=3
##b=5
##for i in range(n,m):
##    c=a+b
##    a=b  
##    b=c
##    print(c)

#------------------------------------------------>
##a="balu"
##b="mounam"
##c=a+b
##l="-"
##
###print(c)
##for i in range(len(c)):
##    if 1<i%3!=0:
##        pass
##        print(c[i]+l,end="")
##    else:
##        print(c[i],end="")

#------------------------------>
##a="balu"
##b="mounam"
##c=a+b
###print(a,b)
##for i in range(0,len(c),3):
##    print(i)
#------------------------------------------------------------->
###Palindrome number

##num=int(input("Enter a number:"))
##temp=num
##rev=0
##while(num!=0):
##    rev=num%10+rev*10
##    num=num//10
##if(temp==rev):
##    print("The number is palindrome!")
##else:
##    print("Not a palindrome!")

#------------------------------------->
###prime number
##n=int(input())
##count=0
##for i in range(1,n):
##    if n%i==0:
##        count=+1
##if count==n:
##    print("prime number!")
##num = 407
##if num == 1:
##    print(num, "is not a prime number")
##elif num > 1:
##   for i in range(2,num):
##       if (num % i) == 0:
##           print(num,"is not a prime number")
##           print(i,"times",num//i,"is",num)
##           break
##   else:
##       print(num,"is a prime number")
##else:
##   print(num,"is not a prime number")
#--------------------------------->
###sum of add nnumber
##n=int(input())
##m=0
##for i in range(n):
##    m=m+i
##print(m)
#----------------------------->
#sum of multy nnumber
##n=int(input("enter:"))
##m=1
##for i in range(1,n):
##    m=i*m
##    print(m)
#-------------------------------------->
##
##while 1:                                  ###leap year.
##    n=int(input('enter the year:'))
##    if n%4==0:
##        print('%d is leap year'%(n))
##    elif n%40==0:
##         print('%d is leap year'%(n))
##    elif n%400==0:
##         print('%d is leap year'%(n))
##    else:
##        print('%d is not leap year'%(n))
#---------------------------------------------------------------------->
##unit=int(input("enter the unit:"))
##if(unit==0): 
##    print("no charge")
##elif(1<=unit<=100):
##    print("Rs 100") 
##elif(101<=unit<=200):
##    result=(100-0)+((unit-100)*2)+100;
##    print("unit",result)
##elif(201<=unit<300):
##    result=(100-0)+((200-100)*2)+((unit-200)*3)+100;
##    print("unit",result)
##else:
##    print("unit exceed.pls contact near by EB office")   
#-------------------------------------------------------------------------------->
##num=int(input("Enter a number:"))
##temp=num
##rev=0
##while(num!=0):
##    dig=num%10
##    rev=rev*10+dig
##    num=num//10
##if(temp==rev):
##    print("The number is palindrome!")
##else:
##    print("Not a palindrome!")
#-------------------------------------------------------------------------->
##n=input("enter:")
##for i in range(len(n)):
##    if n[i]=="a"<=n[i] and n[i]>="z":
##        print(n[i])
#------------------------------------------------------>
# digit count number
##n=int(input())
##c=0
##while (n>0):
##    c=c+1
##    n=n//10
##print(c)
#-------------------------------------------->
# sum of int 
##n=int(input())
##k=0
##for i in range(n):
##    m=n%10
##    k=k+m
##    n=n//10
##print(k)
#------------------------------------>
#dublicate number
##mylist = ["a", "b", "a", "c", "c","c","b","c","a"]
##mylist = list(dict.fromkeys(mylist))
##print(mylist)
#----------------------------------------------------------->
