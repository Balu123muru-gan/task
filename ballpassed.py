def findNextplayer(numberoffriends,friendslist,numberofballpassed,ballpassedlist):
    #print(numberoffriends)
    #print(friendslist)
     #print(numberofballpassed)
    #print(ballpassedlist)
    k1="".join(friendslist)
    print(k1)
    k1=k1+k1[0]
    #print(k1)

    k2="".join(ballpassedlist)
    #print(k2)

    if k2 in k1 :
        print("Direction - Clockwise")
    
        k1=k1.index('d')
        #print(k1)
        k5=k1[:2]
        k6=k1[2:]
        k7=k6+k7
        print(k7)
        print("next player",k7[numberofballpassed%len(k1)])

    """k3=k1[::-1]
    print(k3)
    k4=k2[::-1]
    print(k4)

    if k2 in k3:
        print("Direction - AntiClockwise")
     # print("next player-",k3[numberofballpassed%len(k1)])"""

numberoffriends=int(input())#4
friendslist=[] #  A C D F
for _ in range(numberoffriends):
    friends=input() # ACDF
    friendslist.append(friends)

numberofballpassed=int(input())
ballpassedlist=[]# D F
for _ in range(2):
    passed=input()# D F
    ballpassedlist.append(passed)

findNextplayer(numberoffriends,friendslist,numberofballpassed,ballpassedlist)


