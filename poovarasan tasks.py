
'''for i in range(2, 4):
    for j in range(1, 11):
        if i==j:
            pass
        print(i, "*", j, "=", i*j)
print()'''

'''# Using list comprehension to make
# nested loop statement in single line.
list1 = [ [j for j in range(5)] #[[0,1.2] for i in range(5)]
	     for i in range(3)]
# Printing list1
print(list1)'''
#==================================
'''n=int(input("students:"))

class student():
    def function(self):
        self.name=input()
        self.mark=int(input())
a=[]
for i in range(n):
    o=student()
    o.function()
    a.append(o)
    
    #print(a[i].name,a[i].mark)
for i in range(n):
    for j in range(i+1,n):
        if a[i].name>a[j].name:
            temp=a[i].name
            a[i].name=a[j].name
            a[j].name=temp
for i in range(n):
    for j in range(i+1,n):
        if a[i].mark>a[j].mark:
            temp=a[i].mark
            a[i].mark=a[j].mark
            a[j].mark=temp

choice=int(input("Enter choice:"))
if choice==1:
    for k in range(n):
        print(a[k].name)
elif choice==2:        
    for l in range(n):
        print(a[l].mark)
else:
    print(" Choice Outof Range")'''

#================================
##'''a=input()
##print(list(a))
##b=a.split(" ")
##print(b)
##temp=b[0]
##b[0]=b[-1]
##b[-1]=temp
##print(b)'''

#task 2:

##a=input()
##b=a.split(" ")
##c=len(b)
##for i in range(c-1,-1,-1):
##    print(b[i],end=" ")

#task 3:


##n=['a','c','b','b','c','d','a','f','r','r','a','s','s']
##B=len(n)
##C=[]
##k=0
##S=C.copy()
##print(S)
##for i in range(B):
##    if n[i] not in C:
##        A=C.copy()
##        A.append(n[i])
##    #print(A)
##    elif n[i] in

n=['a','c','b','b','c','d','a','f','r','r','a','s','s']
count=0
##for i in range(len(n)):
##    for j in range(i+1):
##        if n[i]==n[j]:
##            count=count+1
##    print(n[i],count)

##b=set(n)
###print(b)
##c=list(b)
###print(c)
##A={}
##
##for i in range(len(c)):
##    count=0
##    for j in range(len(n)):
##        if c[i]==n[j]:
##            count+=1
##    #print(c[i],count)
##    #print(c[i],":",count)
##    z=({c[i]:count})
##    A.update(z)
##print(A)

#============================================================
n=["a-z"]
print(n)




    



























        
    











