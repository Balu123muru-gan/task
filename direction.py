n=int(input("number of terms:"))
i=0
a=0
b=0
x=0
y=0

for i in range(n):
    #data=["distance","speed","direction"]

    distance=int(input("Enter the distance:")) # 10 20 5 
    speed=int(input("Enter the speed:")) # 50 60 100
    direction=input("Enter the dirction:") # N E S 

    time=(distance/speed)*3600   # (10/50)//3600=720,(20/60)//3600=1200,(5/100)//3600=180
    a+=distance*1000  #a=a+distance=0+10=10,10+20=30,30+5=35
    b+=time #b=b+1 b=0+720,b=720+1200=1920,b=1920+180=2100

    if direction=="N" or direction=="S": # N
        if direction=="N": #N==N
            dir_y=distance*(+1)  # dir_y=10*1=10
        elif direction=="S":
            dir_y=distance*(-1)  #dir_y=5*1=5
        y+=dir_y

    elif direction=="W" or direction=="E": #E
         if direction=="E":
            dir_x=distance*(+1) #dir_x=20*1=20
         elif direction=="W":
            dir_x=distance*(-1)
         x+=dir_x



print(x)
print(y)

if x>0 and y>0:
    print("NE")
elif x<0 and y>0:
    print("NW")
elif x<0 and y<0:
    print("SW")
elif x>0 and y<0:
    print("SE")
elif x>0 and y==0:
    print("E")
elif x==0 and y>0:
    print("N")
elif x<0 and y==0:
    print("W")
elif x==0 and y<0:
    print("S")
elif x==0 and y==0:
    print("orgin")
print(a)
print(b)






























    
    
