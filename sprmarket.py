import math
class item:
    def getitem(self):
        """
        self.itemcode=int(input("enter item code:"))
        self.unitprice=int(input("enter unit price:"))
        self.tax=int(input("enter tax"))
        """
        self.itemcode,self.unitprice,self.tax=[float(i) for i in input().split("|")] #100|30|12   #101|20|0
class selitem:
    def reqitem(self):
        """
        self.ic=int(input("enter item code:"))
        self.qty=int(input("enter qty:"))
        """
        self.ic,self.qty=[int(i) for i in input().split("|")] #100|10
class denomination:
    def den(self):
        """
        self.denamt=int(input("denomination amt:"))
        self.non=int(input("no. of notes:"))
        """
        self.denamt,self.non=[int(i) for i in input().split("|")] #1000|10 #500|10 500|10
#---------------------        
noi=int(input("enter no. of items available in the shop")) #2
itemlist=[]
for _ in range(noi):
    i=item()
    i.getitem()
    itemlist.append(i)
for ans in itemlist:
    print(ans.itemcode,ans.unitprice,ans.tax)
#----------------    
noip=int(input("no. of item purchased by customer"))#1
selitemlist=[]
for _ in range(noip):
    s=selitem()
    s.reqitem()
    selitemlist.append(s)
for ans in selitemlist:
    print(ans.ic,ans.qty)
#---------------------
noden=int(input("no. of denomination:"))#1
denlist=[]
for _ in range(noden):
    d=denomination()
    d.den()
    denlist.append(d)
for ans in denlist:
    print(ans.denamt,ans.non)
#---------------------
cash=float(input("cash paid by the customer:")) #500
#==========output==========
print("==START_BILL==")
for sil in selitemlist:
    for il in itemlist:
        if sil.ic==il.itemcode: #100==100
            wot=il.unitprice*sil.qty #30*10
            ot=(il.unitprice*sil.qty)*il.tax//100 # 30*12/100
            na=wot+ot
            print(sil.ic,"|",il.unitprice,"|",sil.qty,"|",wot,"|",il.tax,"|",ot,"|",na,sep="") #100|30|10|300|12|36|336
            print(wot)#300
            print(ot)#36
            print(na)#336
            nadis=na-(na*10/100)  #336-(336*10/100)
            print(nadis)#302.4
            roudis=math.floor(nadis)
            print(roudis)#302
            print(cash-roudis)#198
print("==END_BILL==")
            
            
            
    





    
    
    
