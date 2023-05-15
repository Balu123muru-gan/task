"""# factorial number
m=int(input())
n = int(input())
fact = 1

for i in range(m ,n+1):
    fact = fact * i
print (fact)"""
#===================
# factorial given value of range
m=int(input())
n=int(input())
for i in range(m,n+1):
    fact=1
    for j in range(i,0,-1):
        if j==1:
            print(j,end="=")
        else:
            print(j,end="*")
            fact*=j
    print(fact)
