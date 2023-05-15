##m=input()
##n=input()
##a=list(m)
##b=list(n)
##print(a)
##print(b)
##
##A=[]
##for i in range (len(m)):
##    for j in range(n):
##        if i==j:
##            A.append(i)
##print(A)


#==========================================================================
Q=[12143,123,456,789,865456]
for i in range(len(Q)):
    A=Q[i]
    C=0
    while A>0:
        B=A%10
        C=C+B
        A=A//10
    #print(C)
    D=C
    E=0
    while D>0:
        F=D%10
        E=E+F
        D=D//10
    print(E)






        













    
