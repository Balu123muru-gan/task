for i in range(1,7):
    for j in range(1,15):
        if j==5 or i+j==13 or (i==1 and 2<j<6) or (j==2 and 1<i<5)or(i==5 and 2<j<6) :
           print(i,j,end="   ")
        else:
            print("",end="      ")
    
    print("\n\n")
