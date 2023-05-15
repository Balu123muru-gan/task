n=int(input())
res=0
for i in range(len(str(n))):
    digit=n%10   # 432%10=2 ,43%10=3,  4%10=4
    res=res+digit # res=0+2 ,res=2+3=5 res=5+4=9
    n=n//10 #432//10=43,43//1=4 ,4//10
print(res) #9
