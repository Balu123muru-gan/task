n=input()
ed=len(n)-1
for i in range(len(n)//2):
    print(n[i],n[ed],end=" ",sep=" ")
    ed=ed-1
if len(n)%2==0:
    print(n[len(n)-1])
