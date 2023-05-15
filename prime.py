s=int(input())
e=int(input())
for i in range(s,e+1):
    for j in range(2,i):
        if(i%j==0):
            print("not a prime")
            break
        else:
            print("prime")
            break
