class Hotel:
    def getdata(self):
        self.id=int(input("hotel id:"))
        self.md=int(input("minimum dur:"))
        self.mdc=int(input("min dur cost:"))
        self.incrd=int(input("incremental duration"))
        self.incrdc=int(input("incremental duration cost"))
        self.famt=int(input("food amt:"))
noh=int(input("no. of hotels:")) #2
hot=[]
for _ in range(noh):
    h=Hotel()
    h.getdata()
    hot.append(h)
#----------------
#for res in hot:
#    print(res.id,res.md,res.mdc,res.incrd,res.incrdc,res.famt)
#----------------
hrsreq=int(input("enter no. of hours required:"))
butamt=int(input("enter budget amt:"))
com=int(input("commission amt:"))
pdis=int(input("premium discount:"))
pn=input("premium /non pre P / N")
tax=int(input("enter tax:"))
food=input("food y/n")
#tips=int(input("enter tips"))
# logic
hcost=[]
hidcost={}
for k in hot:
    cost=k.mdc+ (((hrsreq-k.md)//k.incrd)*k.incrdc)
    #cost=2000+    48-12 // 4 *1000
    totcost=((cost*com)//100)+cost
    #           2200+11000

    if food=='y' or food=='Y':
        totcost=totcost+k.famt
    if pn=='p' or pn=='P':
        totcost=totcost-((totcost*pdis)//100)
    totcost=totcost+((totcost*tax)//100)
    #totcost=totcost+tips
        


    hidcost.update({k.id:totcost})
    hcost.append(totcost)

    
        
hcost.sort() # important

for ans in hcost:
    print(ans)
    if ans<butamt:
        finalamt=ans
    else:
        break
#print("final budget:",finalamt)

hkey=hidcost.keys()
print(hkey)

for key in hkey:
    if hidcost[key]==finalamt:
        print(key,"|",finalamt,sep="")
    print(hidcost[key])


    



               
                          
