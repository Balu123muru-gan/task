##def findNextplayer(numberoffriends,friendslist,numberofballpassed,ballpassedlist):
##    #print(numberoffriends)
##    #print(friendslist)
##    #print(numberofballpassed)
##    #print(ballpassedlist)
##    k1="".join(friendslist)
##    #print(k1)
##    
##    k1=k1+k1[0]
##    #print(k1)
##
##    k2="".join(ballpassedlist)
##    #print(k2)
####    if k2 in k1 :
####        print("Direction - Clockwise")
####    k4=k1.index(ballpassedlist[0])
####    m=k4
####    print(k4)
####    print(m)
####    k5=k1
####    #print(k5)
####    k5=k5[0:len(k5)-1]
####    print(k5)
####    f=k5[m:]
####    s=k5[:m]
####    final=f+s+k2[0]
####    #print(final)
####    print("next player -",final[numberofballpassed%numberoffriends+1])
##    
##     # print("Next player -",k1[numberofballpassed%len(k1)])
##    #---------------------------------------------------------------------------------------------->
##    k3=k1[::-1]
##    print(k3)
##    if k2 in k3:
##      print("Direction - AntiClockwise")
##    print("Next player -",k3[numberofballpassed%len(k1)])
##        
##        
##
##    
##numberoffriends=int(input())#4
##friendslist=[] #  A C D F
##for _ in range(numberoffriends):
##    friends=input() # ACDF
##    friendslist.append(friends)
##
##numberofballpassed=int(input())
##ballpassedlist=[]#  F a
##for _ in range(2):
##    passed=input()#  F a
##    ballpassedlist.append(passed)
##
##findNextplayer(numberoffriends,friendslist,numberofballpassed,ballpassedlist)
##

#----------------------------------------------------------------------------------------------->
def findNextplayer(numberoffriends,friendslist,numberofballpassed,ballpassedlist):
    #print(numberoffriends)
    #print(friendslist)
    #print(numberofballpassed)
    #print(ballpassedlist)
    k1="".join(friendslist)
    #print(k1)#----->#abdcfe
    
    k1=k1+k1[0]
    #print(k1)#----->#abdcfea

    k2="".join(ballpassedlist)
    #print(k2) #---------->#df
    if k2 in k1 :
        print("Direction - Clockwise")
    k4=k1.index(ballpassedlist[0])
    m=k4
    #print(k4)#------------>2
    #print(m)#------------>2
    k5=k1
    #print(k5)#-------->abdcfea
    k5=k5[0:len(k5)-1]
    #print(k5) #------->abdcfe
    f=k5[m:]
    s=k5[:m]
    #print(f)  #------>dcfe
    #print(s)  #------->ab
    z=f+s #---->dcfeab
    z=z[::2] #---->dfa
    #print(z)#----->
    
    final=z+k2[0]
    #print(final)#------>dfad
    print("next player -",final[numberofballpassed%numberoffriends+1])
    
     # print("Next player -",k1[numberofballpassed%len(k1)])
##    #---------------------------------------------------------------------------------------------->
####    k3=k1[::-1]
####    print(k3)
####    if k2 in k3:
####      print("Direction - AntiClockwise")
####    print("Next player -",k3[numberofballpassed%len(k1)])
##        
##        
##
##    
numberoffriends=int(input())#4
friendslist=[] #  A C D F
for _ in range(numberoffriends):
    friends=input() # ACDF
    friendslist.append(friends)

numberofballpassed=int(input())
ballpassedlist=[]#  F a
for _ in range(2):
    passed=input()#  F a
    ballpassedlist.append(passed)

findNextplayer(numberoffriends,friendslist,numberofballpassed,ballpassedlist)
#----------------------------------------------------------------------------------->
##def findnextplayer(numberoffriends,friendslist,numberofballpassed,ballpassedlist):
##    friendslists=[]
##    for i in range(len(friendslist)):#6
##        if i%2==0:#2 4 6
##            friendslists.append(friendslist[i])#a c e
##    #friendslists.append(friendslists[0])
##    r1=''.join(friendslists+friendslists)#ace
##    print(r1)
##    r2=''.join(ballpassedlist)#df
##    print(r2)
##    r3=r1[::-1]
##    if r2 in r1:
##        #print('direction-clock')
##        #print('nextplayer-',r1[numberofballpassed%len(friendslists)])
##        for j in range (len(r1)):
##            if r2[-1]==r1[j]:
##                print('direction-clock')
##                print('nextplayer-',r1[j+1])
##                break
####    if r2 in r3:
####        #print('direction-anticlock')
####        #print('nextplayer-',r3[numberofballpassed%len(r1)])
####        for k in range (len(r3)):
####            if r2[-1]==r3[k]:
####                print('direction-anticlock')
####                print('nextplayer-',r3[k+1])
####                break
##
##numberoffriends=int(input())
##friendslist=[]
##
##for _ in range(numberoffriends):
##    friends=input()
##    friendslist.append(friends)
##
##       
##numberofballpassed=int(input())
##ballpassedlist=[]
##for _ in range(2):
##    passed=input()
##    ballpassedlist.append(passed)
###print(ballpassedlist)
##findnextplayer(numberoffriends,friendslist,numberofballpassed,ballpassedlist)
##
