#py

#1).data types
##a=2
###print(type(a))
##b="balu"
###print(type(b))
##c=2.98
###print(type(c))
##d=True
###print(type(d))
##e='b'
###print(type(e))
#--------------------------------------------
##2),control str
##a=10
##b=20
##print('the add of a&b is:%d',(a,b,a+b))
##print('the add of {0}&{1}is:{2}'.format(a,b,a+b))
##print('the add of {}&{}is:{}'.format(a,b,a+b))

#---------------------------------------------------------------
#3).docment str
##'"\t\t document string"'
##print(__doc__)
##print(1)
##print(2)
##print(3)
##print(4)
##print(5)
##print(6)
#-------------------------------
#4).escape sequence
##print('mounam balu py')
##print('mounam\t balu\t py')
##print('mounam \nbalu\n py')
##print('mounam\\t balu \\tpy')
#----------------------------------------------
#5).end
##print(1,end=" +")
##print(2,end=" +")
##print(3,end=" +")
##print(4,end=" +")
##print(5,end=" +")
##print(6,end=" =")
##print(1+2+3+4+5+6)
#--------------------------------------------
#6).seperator:
##print(1,2,3,4,5,6,7,8,9,sep="\t")
##print(1,2,3,4,5,6,7,8,9,sep="\n")
##print(1,2,3,4,5,6,7,8,9,sep="+")
#---------------------------------------------------
#7).type of py
##a=10
##b=2.5
##c=3.5
##d="b"
##e="balu"
##f=True
##g=False
##print(type(a))
##print(type(b))
##print(type(c))
##print(type(d))
##print(type(e))
##print(type(f))
##print(type(g))
#================================
#8).id method
##a=10
##b=2.5
##c=3.5
##d="b"
##e="balu"
##f=True
##g=False
##print(id(a))
##print(id(b))
##print(id(c))
##print(id(d))
##print(id(e))
##print(id(f))
##print(id(g))
#--------------------------------------------------------------
#9).arithmetic operator
##a=10
##b=20
##print(a+b)
##print(a-b)
##print(a*b)
##print(a/b)
##print(a//b)
##print(a%b)

#==============================
#10).Relation operator
##a=10
##b=5
##print(a>b)
##print(a<b)
##print(a<=b)
##print(a>=b)
##print(a==b)
##print(a!=b)
#==============================
#11).logical operator
##a=3
##b=5
##c=2
##print(a>b and c<a)
##print(b>a and c<a)
##print(b>a or c<a)
##print(a>b or b<a)
##print(not(a>b or b<a))
##print(not(b>a or c<a))
      
#=======================
#$12).assingment operator
"""a=5
a+=3
#print(a)
a-=3
#print(a)
a*=3
#print(a)
a//=2
#print(a)
a=9
a/2
##print(2)
a%2
print(a)"""
#=============================
#13.special operator
#1)membership
##a="pen"
##print(pen in a)
#2)identify operator
#
#=============================
#14).data structure
#1)List
##a=[1,2,3,4,5,6,7,4,3,2,1]
##print(a[5])
##print(a[-3])
##print(a[0])

#nested list( list inside another inside)
##a=[1,2,3,[4,5,6],[1,2,3],[18,23,42]]
##print(a[3])
##print(a[3] [1])
##print(a[5])
##print(a[5][0])
##print(a[-2])
##print(a[-2][-2])
#========================================
#2).Tuple
##a=(1,2,3,4,4,5,3,2)
###print(a)
##print(a[-3])
##print(a[2])
##print(a[-1])
##a=(1,2,3,(4,5,(6,7),8,9),10)
##
##print(a[-3])
##print(a[3][2][1])
#-------------------------------------------------------------------------
#3)set

##a={5,3,9,5,12,3,1,0}
#print(a)
##print(a[2])
#unordered
#immutable
#noiterable
#only universe
#===========================
#4).dic
#key        #value
#immutable  #mutable
#not interable #interable
#orderd
#not allow #alow dublicate
##a={1:11,2:22,3:33,4:44,5:55,6:66}
##print(a[2])
##print(a[4])
##a[2]=17
##print(a)
##a={1:11,1:22,1:33,2:44,3:44,4:55}
##print(a)
#a={1:"arun",2:"prem",3:"prem",4:"ramesh",1:"sam"}
#print(a)
#-----------------------------------------------------------------------------------
#15).Slicing----->
#a="bettervisibility"
##print(a[:])
##print(a[: :])
##print(a[2:10])
##print(a[3:13])
##print(a[3:4])
##print(a[4:])
##print(a[3:13])
#print(a[-3:-13])
##print(a[: :3])
#print(a[2:11:2])
#b="confidential"
#print(b[:8])
#print(b[-8:8 ])
#print(b[2:-2])
##print(b[3:3])
##print(b[8::3])
#print(b[:10 :-10])
#------------------------------------
#16).Run and time value
##m=int(input(" enter"))
##n=int(input("enter2:"))
##print(m+n)\
##m=input(" enter")
##n=input("enter2:")
##print(m+n)
#chr,float,str,int
#=============================
#17).control statement
#1) simple if
##mark=int(input("enter:"))
##if (34<mark<101):
##    print("pass")
#------------------------------------
#2).if else
##mark=int(input("enter:"))
##if (34<mark<101):
##    print("pass")
##else:
##    print("fail")
#------------------------------
#3). elif
##pwd=int(input("enter"))
##if pwd==123:
##    print("ready to access")
##elif pwd==456:
##    print("ready to access")
##elif pwd==789:
##    print("ready to access")
##elif pwd<100 or pwd>999:
##    print("enter three digit")
##else:
##    print("invalid credential")
#--------------------------------------------------
#4).nested if
##t=int(input("enter tamil:"))
##e=int(input("enter eng:"))
##m=int(input("enter maths:"))
##s=int(input("enter sce:"))
##ss=int(input("enter sce:"))
##
##if t>34 and e>34 and m>34 and s>34 and s.s>34:
##    print("pass")
##else:
##    print("fail")
##total=t+e+m+s+ss
##awg=total/5
##    if awg>90:
##        print("A grade")
##    elif awg>80:
##        print("B grade")
##    elif awg>70:
##        print("C grade")
##    elif awg>60:
##        print("D grade")
##    else:
##        print("no grade due to fail")
#================================================
#)18).loop
#1)while loop
# 2)forward loop
##i=1
##while i<=10:
##    i+=1
##    print(i)

#backward loop
##i=10
##while i>=1:
##    i-=1
##    print(i)

##sum=1
##i=10
##while i>=1:
##    if i==1:
##        print(i,end="=")
##    else:
##        print(i,end="*")
##    sum*=i
##    i-=1
##print(sum)
    

##sum=1
##i=1
##while i<=10:
##    if i==10:
##        print(i,end="=")
##    else:
##        print(i,end="*")
##    sum*=i
##    i+=1
##print(sum)

#infinte loop

##i=1
##while True:
##    print("balu")
##i=1
##while 26789:
##    print("ajith")

#run prgm
##i=int(input("enter:"))
##while i!=0:
##    print(i)


#task method
##i=int(input("enter:"))
##sum=0
##while 1!=0:
##    sum+=i
##    i=int(input("enter:"))
##print(i)
#-----------------------------------------------------------------------------
#2) for loop
# forward 
##for i in range(1,11):
##    print(i,end=" ")
##print()

#backward
##for i in range(10,0,-1):
##    print(i,end=" ")
#==============================
#ex. sum of digit 
##sum=0
##for i in range(1,11):
##    if i==10:
##        print(i,end="=")
##    else:
##        print(i,end="+")
##        sum+=i
##print(sum)
#------------------------------------------------------
# multiplay of num
##sum=1
##for i in range(1,11):
##    if i==10:
##        print(i,end="=")
##    else:
##        print(i,end="*")
##        sum*=i
##print(sum)
#------------------------------------------------------------
#Nested for loop
##for i in range(6):
##    for j in range(6):
##        print(i,j,end=" ")
##    print()

#ex.2
##for i in range(6):
##    for j in range(6):
##       # print(i,j,end=" ")
##       if (i==0 or j==0 or i==5 or j==5):
##            print("*",end="")
##       else:
##           print(end="   ")
##    print()
#=================================================
#ex.3 --->
##k=1
##for i in range(6):
##    k=i
##    for j in range(6):
##        print(k,end="  ")
##        k+=5
##    print()
#-------------------------------------------------------------------------
#ex.4----->
##for i in range(1,6):
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print()
#---------------------------------------------------
#ex.4--------->
##for i in range(6,0,-1):
##    for j in range(i-0):
##        print("*",end=" ")
##    print()
#-------------------------------------
#ex.5----->
##for i in range(6):
##   
##    for j in range(6):
##        if(i>=j):
##            print("*"end=" ")
##        else:
##            print(" ",end=" ")
##
##    print()
#==========================
#6----->
##for i in range(6):
##    for j in range(6):
##        if(i<=j):
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()
#----------------------------------------------------->
#7----->
##for i in range(6):
##    for j in range(6):
##        if(i+j<=5):
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()
#--------------------------------------------------->
#8-------------->
##for i in range(6):
##    for j in range(6):
##        if(i+j>=5):
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()
#-------------------------------------------------------->
#9)------> bending tassk
##for i in range(6):
##    k=0
##    y=1
##    for j in range(1,i+i):
##        if(y<=i):
##            k+=1
##            print(k,end=" ")
##        else:
##            k-=1
##            print(k,end=" ")
##    y+=1
##    print()
#-------------------------------------------------------------->
#10)--------->
##k=21
##for i in range(6):
##    for j in range(6):
##        if(i+j>=6):
##            print(k,end="    ")
##            k+=1
##        else:
##            print(" ",end="  ")
##    print()
#----------------------------------------------------------->
#11)----------->
##k=2949
##for i in range(6):
##    for j in range(6):
##        if(i+j>=6):
##            print(chr(k),end=" ")
##            k+=1
##        else:
##            print(" ",end=" ")
##    print()
#------------------------------------------------------------>
#19)...jumping statement
      #it help to skip the statement
#1)break------->when you stop iteration used to break method
#2)continue----->when you skip the iteration used to continue method
#3)pass----->when you no change used to pass method



###1)break
##for i in range(1,11):
##    if(i==6):
##        break
##    print(i)
##print("program end")

###2)continue
##for i in range(1,11):
##    if i==6:
##        continue
##    print(i)

#3)pass
##for i in range(1,11):
##    if i==6:
##        pass
##    print(i)
#---------------------------------------------------------------->
#20)errors-------->

#1) name error---->
##a=10
##print(c)

#o/p---->NameError: name 'c' is not defined

#2)value error
##a=int(input("enter:"))
##print(a)

#o/p---->ValueError: invalid literal for int() with base 10: 'balu'

#3)type error
##a=10
##b="balu"
##print(a+b)

# print(a+b)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

#4)index erorr
##a=[11,22,33,55,44,66]
##print(a[10])
##print(a[3])

#IndexError: list index out of range
#

#5)...key erorr
##a={1:11,2:22,3:33,4:44}
##print(a[10])

#KeyError: 10

#6).syntax error
##a={1:11,2:22,3:33,4:44}
##print(a[10]

      # ) not closed so its syntax error

#7)indented error

##m=int(input("enter:"))
##if m>34:
##    print("pASS")
##else:
##print("fail")

#o/p---->excepted to intended block in else

#8)Zero division error

##a=3
##c=0
##print(a/c)

#o/p----->ZeroDivisionError: division by zero

#9)key board interupt error

##while True:
##    print("balu")

      #------------------------------------------------------>
#21).function method

      #2) types
      #1)build in fuctions



#1) string---> group of letter
##
##a="balamurugan"
##print(a.upper())
##print(a.lower())
##print(a.casefold())
##print(a.isupper())
##print(a.islower())
##print(a.title())
##print(a.capitalize())
##print(a.istitle())
##print(a.isalpha())
##print(a.isnumeric())
##print(a)
##print(a.isalnum())
##b="123"
##print(b.isnumeric())
##print(b.isspace())
##print(a.center(50))
##print(a.count('a'))
##print(a.find('g'))
##print(a.rfind('a'))
##print(a.find('a'))
##print(a.index('m'))
##print(a.index('n'))
##a="b+a+l+a"
##print(a.split('|'))

##c="isidentifier"
##print(c)

##a="apple"
##print(a.startswith('app'))
##print(a.endswith('e'))

##n= "i am karur"
##print(n.replace("karur","chennai"))

#2)random function
#1) random
"""
import random
print(random.random())
#2)uniform
import random
print(random.uniform(1,2))

#3) randint
import random
print(random.randint(1,5))
#4)choice
import random
choc=['balu','5 star','dairy','milk']
print(random.choice(choc))

#5)sample
import random
choc=['balu','5 star','dairy','milk']
print(random.sample(choc,3))
#6)shuffle
import random
choc=['balu','5 star','dairy','milk']
print(random.shuffle(choc))"""

#3) math random






#---------------------------------------------------------------.
#22)data structure

#1)list
a=[1,2,44,6,5,7,33,2,1]
##c=a
##print(c)
##print(a.pop(4))
##c=a.copy()
##print(c)
##c.clear()
##print(c)
##a.sort()
##print(a)
##a.append(55)
##print(a)
##b=[99,88,77,66,33,22]
##a.extend(b)
##print(a)
##print(a.insert(5,46))
##print(a)
##print(len(a))
##print(min(a))
##print(max(a))
##print(a.pop(4))
##print(sum(a))
##a.reverse()
##print(a)
##a.sort()
##print(a)
##del a[5]
##print(a)
##dir(a)
##print(a)

##b=(1,5,3,8,5,2,9,0)
##print(b.count(5))
##print(b.index(8))
 ##
##print(type(b))
##print(min(b))
##print(max(b))
##print(sum(b))
##print(len(b))
##print(sorted(b))

#------------------------------------------>
#3) set
##m={4,3,7,5,0,7,1,9,7}
##print(m)#------> dublicate not support
##print(len(m))
##print(sum(m))
##print(max(m))
##print(min(m))
##print(sorted(m))
##print(round(7))
##print(m.remove(5))
##print(m)
##print(sum(m))

#a={2,3,5,6,4,2}
##a.remove(5)
##print(a)
##c=a.copy()
##print(c)
#d={4,5,6,7,8}
##c.difference(d)
##print(a)
##a.add(10)
##print(a)
##a.update(d)
##print(a)
#a.intersection(d)
#print(a)
#---------------.------------------------>

###4)dictionary
##a={1:11,2:22,3:33,4:44,5:55}
####c=a.copy()
####print(c)
####c.clear()
####print(c)
####print(a)
####a.popitem()
####print(a)
##a.keys()
##a.values()
##print(a)
##print(a)

#----------------------------------------------------->
#2) user defined fuctions
#1)no arguments no return
##def fun():
##    a=4
##    b=5
##    print(a+b)
##    print(a-b)
##    print(a*b)
##    print(a%b)
##fun()

#2)no argument with return types
##def fun():
##    a=4
##    b=7
##    return a+b
##print(fun())

#3)with argument with return types
##def fun(a,b,c):
##    return a+b+c
##print(fun(1,2,3))
##print(fun(1,2,3)+100+200)

#4)with argument no return types
##def fun(a,b,c):
##    print(a+b+c)
##fun(1,2,3)


#-------------------------------------------------------------------------------------->
#23)positional argument
##def fun(a,b,c):
##    print(a,b,c)
##fun(1,2,3)
      

#24)default argument
##def fun(a=10,b=20,c=30):
##    print(a,b,c)
##fun(1,2,3)
##fun(1,2)
##fun(1)
##fun()

#25)keyword argument
##def fun (a,b,c):
##    print(a,b,c)
##fun(b=2,c=8,a=1)

#26) orbitary argument

##def shoping(name,*products):
##    print('hi',name,'the product u are purchased are:')
##    k=1
##    for i in products:
##        print('%d)%s',(k,i))
##        k+=1
##shoping('renga','rose','ajith','bike')
    
  #=======================================
# math funtion
##import math
##x=5.4
##print(math.floor(x))
##print(math.ceil(x))
##print(math.factorial(10))
##print(math.gcd(4,2))
##print(math.sqrt(2))
##print(math.isqrt(2))
#----------------------------------------------------
#27)recursion
#it is act like a loop
#the function calling its self .ints infinte
##def rec(n):
##    if n==10:
##        print(n,end=' ')
##        return rec
##    else:
##        print(n,end=' ')
##        return rec(n+1)
##print(rec(1))

#===============================
#29)lambda fuction
# single line speciafility
#anonymoun fuc
###variable name do not set easily
##a=lambda x,y,z:x+y-z
##print(a(4,3,2))
##
##data=[1,2,3,4,56,7,8,9]
##a=tuple(map(lambda x:x*x,data))
##print(a)

##data=[1,2,3,4,5,6,7,8]
##for i in map(lambda x:x*x,data):
##    print(i)

##data=[1,2,3,4,5,6,7,8,9]
##c=[]
##for i in filter(lambda x:x%2==0,data):
##    c.append(i)
##print(tuple(c))

##data=[1,2,3,4,5,6,7,8,9]
##c=[]
##for i in filter(lambda x:x%2==1 and (x>2 and x<4),data):
##    c.append(i)
##print(tuple(c))
##
##def fun(n):
##    return lambda x:x+n
##z=fun(10)
##print(z(90))

#-------------------------------------------------------------------------->
#30) global variable

#global variable in use continue the previous value at  inside the function
#a=10
#print(a)
##def fun():
##    a=20
##    print(a)
##fun()
##print(a)

##def fun():
##    global a
##    a=20
##    print(a)
##fun()
##print(a)
#---------------------------
import random

print(random.randrange(1, 10))
