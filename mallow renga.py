##s=int(input())          #factorial.
##e=int(input())
##for i in range(s,e+1):
##    fact=1
##    for j in range(i,0,-1):
##        if j==1:
##            print(j,end='=')
##        else:
##            print(j,end='*')
##        fact*=j
##    print(fact) 


##s=int(input())         #fibonacci        
##e=int(input())
##f1=-1
##f2=1
##for i in range(s,e+1):
##    f3=f1+f2
##    if f3>s and f3<e:
##        print(f3,end=',')
##    f1=f2
##
##    f2=f3
##--------------------------------------------
##f=list(input())     #to eliminate same letters.
##s=list(input())
####print(f)
####print(s)
##for i in range(len(f)):
##  for j in range(len(s)):
##        if f[i]==s[j]:
##            f[i]=''
##            s[j]=''
##print(f)
##print(s)
##f1="".join(f)
##f2="".join(s)
##print(f1)
##print(f2)
##total=len(f1)+len(f2)
##print(total)

##min three low value.py
    
##a="renganathan"
##b=list(a)
##print(b)
##c=''.join(b)
##print(c)

##n=list(input())     #find index of character.
##c=input()
###print(n)
##x=-1
##A=[]
##for i in range(len(n)):
##    x+=1
##    if n[i]==c:
##        A.append(x)
##        
##print(c,'indexe are:',A)

##x=list(input())     #to neglate the space.
##print(x)
##for i in range(len(x)):
##    if x[i]==' ' and x[i+1]==' ':
##        continue
##    else:
##        print(x[i],end='')


##a=input()        #insert word inside the index.
##b=input()
##c=int(input())
##x=list(a)
###print(x)
##y=len(x)
###print(y)
##if c<=y:
##    x.insert(c,b)
##    #print(x)
##    m="".join(x)
##    print(m)
##else:
##    print(c,"is out of range")


##a=input()
##b=input()
##c=int(input())
##x=list(a)
##print(x)
##y=len(x)
##if c<=y:
##    x.append('')
##    for i in range(y,c,-1):
##        x[i]=x[i-1]      
##    else:
##        print('invalid index')
##x[c]=b
##print(x)
##z=''.join(x)
##print(z)

##class sample:
##    def fun(self,data,data1,n):
##        print(data[:n]+data1+data[n:])
####n=int(input())
##obj=sample()
##print(obj.fun('renganathan','ajith',0))

'''a=input()
b=input()
c=int(input())
'''
##class direction:
##    def data(self):
##        dis=int(input())
##        speed=int(input())
##        dir=input()
##n=int(input('laps:'))
##A=[]
##for i in range(n):
##    obj=direction()
##    obj.data()
##    A.append(obj.data)
##print(A)

"""n=int(input('number of labs:'))
for i in range(n):
    dis=int(input())
    speed=int(input())
    dir=input()
    time=(dis/speed)*3600
    if dir=='N':
        dir_y=dis*(+1)
    elif dir=='S':
        dir_y=dis*(-1)
    elif dir=="E":
        dir_x=dis*(+1)
    elif dir=='W':
        dir_x=dis*(-1)"""

##class vowels:
##    def data(self):
##        n=input()
##a=int(input('how mwny lwtters:'))
##A=[]
##for i in range(a):
##    obj=vowels()
##    obj.data()
##    A.append(obj.data())
###n=input()
##print(A)


##a=[1,2,2,3,4,4,5,6,6,6,7,7,7]
##b=len(a)
##print(b)
##for i in range(len(a)):
##    for j in range(i+1,len(a)):
##        if a[i]==a[j]:
##            a[i]=" "
##            if a[i]=="":
##                a.remove(a)
##print(a)
##c=tuple(a)
##print(c)
##x=str(a)
##print(x)
##y="".join(c)
##print(y)


'''class slot:
    def slotdata(self):
        self.date=int(input())
        self.sid=int(input())
        self.nosheet=int(input())
class student:
    def studdata(self):
        self.studid=int(input())
        self.studcut=int(input())
        self.studage=int(input())
        self.studhsc=int(input())
        self.studsslc=int(input())
        self.cdate=0
        self.cslotid=0

n=int(input())
A=[]

for _ in range(n):
    s=slot()
    s.slotdata()
    A.append(s)
for j in range(len(A)):
    print(A[j].date)
    print(A[j].sid)
    print(A[j].nosheet)
a=int(input())
B=[]
for _ in range(a):
    st=student()
    st.studdata()
    B.append(st)
fsid=int(input())
for k in range(a):
    print(B[k].studid)
    print(B[k].studcut)
    print(B[k].studage)
    print(B[k].studhsc)
    print(B[k].studsslc)
for i in range(a):
    for j in range(i+1,len(a)):
        if B[i].studcut < B[j].studcut:
            temp=B[j].studcut
            B[j].studcut=B[i].studcut
            B[i].studcut=temp
for i in range(a):
    for j in range(i+1,len(a)):
        if B[i].studcut==B[j].studcut:
            if B[i].studage < B[j].studage:
                temp=B[j].studcut
                B[j].studcut=B[i].studcut
                B[i].studcut=temp
for i in range(a):
    for j in range(i+1,len(a)):
        if B[i].studcut==B[j].studcut:
            if B[i].studage==B[j].studage:
                if B[i].studhsc < B[j].studhsc:
                    temp=B[j].studcut
                    B[j].studcut=B[i].studcut
                    B[i].studcut=temp
for i in range(a):
    for j in range(i+1,len(a)):
        if B[i].studcut==B[j].studcut:
            if B[i].studage==B[j].studage:
                if B[i].studhsc==B[j].studhsc:
                    if B[i].studsslc < B[j].studsslc:
                        temp=B[j].studcut
                        B[j].studcut=B[i].studcut
                        B[i].studcut=temp
noofsheet=0
for i in range(len(A)):
    noofsheet=noofsheet+A[i].nosheet
print('total no of sheet:',noofsheet)
a=0
if a<=noofsheet:
    for i in range(len(A)):
        for j in range(slot[i].nosheet):
            B[a].cdate=slot[j].date
            B[a].cslotid=slot[j].slotid
            a+=1
            if a==len(B):
                break
for i in range(a):
    if fsid==B[i].id:
        print(B[i].cdate,"|",fsid,"|",B[i].cslotid,sep=',')'''
    
        

'''class hotels:
    def hdata(self):
        self.hid=int(input('id:'))
        self.mindur=int(input('mindur:'))
        self.mdc=int(input('mdc:'))
        self.incd=int(input('incd:'))
        self.idc=int(input('idc:'))
        self.food=int(input('food:'))
n=int(input('nuber:'))
hot=[]
for i in range(n):
    hotel=hotels()
    hotel.hdata()
    hot.append(hotel)

for j in range(n):
    print(hot[i].hid)
    print(hot[i].mindur)
    print(hot[i].mdc)
    print(hot[i].incd)
    print(hot[i].idc)
hrcus=int(input())
budamt=int(input())
comamt=int(input())
predis=int(input())
premium=input()
tax=int(input())
food=input()
A=[]
B={}
for k in hot:
    cost=hot.mdc+((hot.hrcus-hot.mindur)//hot.incd)*hot.idc   #cost
    cost=(cost*hot.comamt)//100+cost           #comamt

    if premium=='Y' or premium=='y':     #premium
        cost=cost-((cost*predis)//100)
    else:
        pass

    cost=((cost*tax)//100)+cost     #tax


    if food=='Y' or food=='y':
        cost=cost+food
    else:
        pass
    print('total cost is:',cost)
    A.append(cost)
    B.append({K.id:cost})
A.sort()
for i in A:
    if i<butamt:
        final_amount=i
key=B.keys()
for a in key:
    if B(a)==final_amount:
        print(a,"|",final_amount,sep='')'''
    




##n1=int(input('enter your first number:'))    #biggest number.
##n2=int(input('enter your second number:'))
##n3=int(input('enter your third number:'))
##if n1>n2:
##    if n1>n3:
##        print('n1 is biggest number')
##    else:
##        print('n3 is biggest number')
##elif n2>n3:
##    print('n2 is biggest number')
##else:
##    print('n3 is biggest number')

##a=[23,65,88,54,33,8,864,65,23]      ####biggest number
##b=a[0]
##d=a[0]
##e=a[0]
##c=[]
##for i in a:
##    if i>b:
##        b=i            
##c.append(b)
##
##
##for i in a:
##    if (i>d and i!=b):
##        d=i
##c.append(d)
##print(c)
##
##for i in a:
##    if i>e and i!=b and i!=d:
##        e=i
##c.append(e)
##print(c)

##x=int(input('enter your number:'))      ###fact with range.
##y=int(input('enter your number:'))
##for i in range(x,y):
##    fact=1
##    print(i,end=':')
##    for j in range(i,0,-1):
##        
##        if j==1:
##            print(j,end='=')
##        else:
##            print(j,end='*')
##        fact*=j
##    print(fact)


"""while 1:                                  ###leap year.
    n=int(input('enter the year:'))
    if n%4==0:
        print('%d is leap year'%(n))
    elif n%40==0:
         print('%d is leap year'%(n))
    elif n%400==0:
         print('%d is leap year'%(n))
    else:
        print('%d is not leap year'%(n))"""

##a=input()      ###assending with name.
##b=list(a)
###print(b)
##for i in range(len(b)):
##    for j in range(i,len(b)):
##        if b[i]>b[j]:
##            temp=b[j]
##            #print(temp)
##            b[j]=b[i]
##            #print(b[j])
##            b[i]=temp
##            #print(b[i])
###print(b)
##k="".join(b)
##print(k)

        
        

##n=input()
##print(n)
##a=n.split(' ')
##print(a)
##b=len(a)
##for i in range(len(a)):
##    A=a[i]
##    #print(A)
##    B=list(A)
##    #print(B)
##    for j in range(len(B)):
##        for k in range(len(B)):
##            pass
##        print(B[k],end='')
##        B.pop()
##    print(end=' ')


##n=int(input('enter your number:'))       #pattern.
##k=1
##for i in range(n):
##    for j in range(1,i+2):
##        print(k,end=' ')
##    print()
##    k+=1

##n=int(input('enter your number:'))      #pattern.
##for i in range(n):
##    k=0
##    for j in range(i+1):
##        k+=1
##        print(k,end=' ')
##    print()

'''k=1
n=int(input('enter your number:'))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(k,end=' ')
    print()
    k+=1'''

##n=int(input('enter your number:'))
##k=n
##
##for i in range(n,0,-1):
##    for j in range(i):
##        print(k,end=' ')
##    print()


'''class emp:
    def getinfo(self):
        self.emp_no=int(input("enter emp no:"))
        self.emp_name=input("enter emp name:")
        self.emp_sal=int(input("enter emp salary:"))
    def display(self):
        print("employe number:",self.emp_no)
        print("employe name:",self.emp_name)
        print("employe salary:",self.emp_sal)
list=[]
n=int(input("enter no.of employee:"))
for i in range(n):
    student=emp()
    list.append(student)
    student.getinfo()
for i in range(n):
    print(list[i].emp_no,list[i].emp_name,list[i].emp_sal)
c=0
for i in range(n):
    if list[i].emp_sal > c:
        c=list[i].emp_sal
        name=list[i].emp_name
        id=list[i].emp_no
print(c,"||",name,"||",id)'''

##n=int(input("enter your number:"))
##space=n-1
##for i in range(0,n):
##    for j in range(0,space):
##        print("",end=" ")
##    for k in range(0,i+1):
##        print("*",end=" ")
##    print()
##    space-=1
##'''for A in range(0,n):
##    space+=1
###print(space)'''
##space=n-1
##for x in range(n-1):
##    for y in range(0,n-space):
##        print("",end=" ")
##    for z in range(space,0,-1):
##        print("*",end=" ")
##    space-=1
##    print()


##n=int(input("enter your number:"))     ###pattern   A
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if ((i==1 and 1<j<n) or (j==1 and i>1)  or (j==n and i>1) or i==5):
##            print("*",end="")
##        else :
##            print(" ",end="")
##    print()




##while True:
##    n=int(input("enter your number:"))
##    A=n//2
##    for i in range(1,n+1):
##        for j in range(1,n+1):
##            if ((i==1 and j>2) or (i==n and j<n) or (i==A and (1<j<n)) or (1<i<A and j==1) or (A<i<n) and j==n)):
##                print("*",end="")
##            else:
##                print(" ",end="")
##        print()



##def renga(R,T):
##    for k in range(R,T):
##        if k==R or k==T-1:
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()
##n=int(input("enter your number:"))
##space=n-1
##for i in range(0,n):
##    for j in range(0,space):
##        print("",end=" ")
##    renga(R=0,T=i+1)
##    space-=1
##space=n-1
##for x in range(n-1):
##    for y in range(0,space):
##        print("",end=" ")
        


##n=int(input(" "))
##i=1
##
##while(i<=n):
##    j=1
##    while(j<=n):
##        if (i==j or i+j==8):
##            print("@",end=" ")
##        else:
##            print("  ",end="")
##        j=j+1
##    i=i+1
##    print()  

##n1=input("first name:")
##n2=input("second name:")
##X=list(n1)
##Y=list(n2)
##A=len(n1)
###R=print(X[A-1])
##B=len(n2)
###T=print(Y[B-1])
##for i in range(A):
##    print(X[i],end=" ")
##    for j in range(B):
##        pass 
##    print(Y[j],end=" ")
##    B=B-1

##id=input("enter amail id:")
##n=int(input("enter min char:"))
##A=print(len(id))
##spe_char=0
##alpha=0
##num=0
##if n <= len(id):
##    for i in id:
##        if i.isalpha()==True:
##            alpha=alpha+1
##        elif i.isnumeric()==True:
##            num=num+1
##        else:
##            spe_char=spe_char+1
##print("alpha in id is:",alpha)
##print("num in id is:",num)
##print("spe_char in id is:",spe_char)
##else:
##    print("please enter min 8 char")

##import threading
##def fun(name):
##    for i in name:
##        print(i,end="")
##def fun1(name):
##    B=list(name)
##    #print(B)
##    A=len(name)
##    #print(A)
##    for j in range((A-1),-1,-1):
##        print(B[j],end="")
##n1=input("name:")
##n2=input("names:")
##t1=threading.Thread(target=fun,args=(n1,))
##t2=threading.Thread(target=fun1,args=(n2,))
##t1.start()
##t2.start()



a=["1223python8786","345jango878","1342jdfkrjf78434"]
q=[]
w=[]
R=[]
T=[]
for i in a:
    #print(i)
    A=i
    #print(A)
    for j in range(len(A)):
        if A[j].isalpha()==True:
            R.append(A[j])
            print(R)
        else:
            T.append(A[j])
    print(T)
    C=" ".join(T)
    #print(C)
    w.append(C)
    T.clear()
    B=" ".join(R)
    q.append(B)
    R.clear()
print(q)
print(w)

##name=input("name:")
##n=int(input("number:"))
##print((name*n))

"""
id=input("enter your e mail id:")
min=int(input("min:"))
#max=int(input("max:"))
a=len(id)
upp_case=0
low_case=0
num=0
spl_char=0
if min<=len(id):
    for i in id:
        if i.isalpha()==True:
            if i.isupper()==True:
                upp_case+=1
            else:
                low_case+=1
        elif i.isnumeric()==True:
            num+=1
        else:
            spl_char+=1
    print(upp_case)
    print(low_case)
    print(num)
    print(spl_char)
    if (1<=upp_case and 1<=low_case and 1<=num and 1<=spl_char):
        print("valid E-mail id")
    else:
        print("invalid E-mail id")
    
else:
    print("please enter min 8 charactor")
    """


##n=['e','r','d','a','q','e','t','g','f','d','w','w','f','d','w','q','w','e','t','e']
##A=[]
##for i in range(len(n)):
##    A_i_i=[]
##    if n[i] in n:
##        A_i_i=A.copy()
##        if n[i].islist==True:
##            #A_i=A.copy()
##            A_i_i.append(n[i])
##            #print(A_i)
##        else:
##            A_i_i=A.copy()
##            A_i_i.append(n[i])
##            #print(A_i)
##    
##for i in range(len(n)):
##    print("count is:",A_i_i)
##        
##        
##

##
##row=int(input())
##for i in range(row,0,-1):
##    for j in range(row-i):
##        print("",end="")
##    for j in range(1,2*i):
##        print("*",end="")
##    print()

##for i in range(1,row+1):
##    for j in range(row-i):
##        print(" ",end="")
##    for j in range(1,2*i):
##        print("*",end="")
##    print()


##a=25
##b=10
##print(id(a))
##print(id(b))

##import keyword
##print(keyword.kwlist)
        
##
##for i in range(10,1,-2):
##    print(i)
            
##print(list(range(5)))
##print(list(range(2,5)))
##print(list(range(1,21,1)) )

##for i in range(3):
##    a=int(input("enter:"))
##    b=int(input("enter:"))
##    print(a+b)

##for i in range(5):
##    for j in range(i+1):
##        print("*",end="")
##    print()
##
##print("---------------------")
##for i in range(5,0,-1):
##    for j in range(i):
##        print("*",end="")
##    print()

##for i in range(65,70,1):
##    print(chr(i))
    
##for i in range(97,102):
##    print(chr(i))

##a=97
##b=102
##
##while a<=b:
##    print(chr(a))
##    a+=1

for i in range(65,70,-1):
    for j in range(65,70,1):
        print(chr(j+1),end="")
    print()
                    



















