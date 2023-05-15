
print("welcome to ATM machine")
pin=int(input("enter your 4 digit pin:"))
amt=5000
if (pin == 6381):
    print("1-withdraw")
    print("2-deposit")
    print("3-Balance enquiry")
    print("4-Fast cash")
    choice=int(input("please choose transaction:"))
    if (choice==1):
        w=int(input("Enter withdraw amount:"))
        if (w<amt and w%100==0):
            wa=amt-w
            print("Take your cash:",wa)

        else:
            print("Invalid cash")

    if (choice==2):
        d=int(input("Enter your deposite amount:"))
        dd=amt+d
        print("After deposite amt:",dd)

    if (choice==3):
        print("your available amount:",amt)

    if (choice==4):
        print("1->1000")
        print("2->2000")
        print("3->5000")
        print("4->10000")
        op=int(input("Enter your fast cash option:"))
        if (op ==1 and 1000<amt):
            print("Take your cash 1000")
        elif (op==2 and 2000<amt):
            print("Take your cash 2000")
        elif (op==3 and 5000<amt):
            print("Take your cash 5000")

        elif (op==4 and 10000<amt):
            print("Take your cash 10000")

        else:
            print("Invalid Fast case option")
else:
    print("Wrong pin number")
  

'''    
class Customer: #class created
    ATM="Welcome to State Bank ATM..............."#static method
    # construtor        default value added
    def __init__(self,name,pin=6381,balance):
        self.=name# instance variable 
        self.balance=balance # balance did'nt add because default value 

    def deposit(self,amount):
        self.balance=self.balance+amount # (self)instance variable used,so that is instance method
        print("after deposit amount:",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds can't perform")

        else:
            self.balance=self.balance-amount
            print("after deposit amount:",self.balance)
print("welcome to:",Customer.bankname)
name=input("enter your bank:")
c=Customer(name)#class object will be created
 
while True:# all contions true this loop will be executed
    print("d-deposit\w-withdraw\e-exit")
    option=input("your choice")
    if option.lower()=='d': #put d or D
        amount=float(input("enter amount to deposit:"))
        c.deposit(amount)

    elif option.lower()=='w':#put w or W
        amount=float(input("enter amount to withdraw:"))
        c.withdraw(amount)

    elif option.lower()=='e': #put e or E
        print("poda veliya") 
        break
    else:
        print("your option is invalid plz choose crt option")
'''

'''
print("sumathy bakery")
veg_foods=int(input("veg:"))
tea=15
coffee=20
eggbuffs=17
mushroombuffs=19
vegbuffs=15


while True:
    if (veg_foods==1):
        print("1-tea")
        print("2-coffee")
        print("3-egg buffs")
        print("4-mushroom buffs")
        print("5-veg buffs")
        print("6-TOTAL BILL=")
        A=int(input("which food you eats:"))
        if (A==1):
            AA=int(input("how many teas:"))
            T=AA*tea
            print("your tea bill",T)

        elif (A==2):
            BB=int(input("how many coffee's:"))
            C=BB*coffee
            print("Your Coffee Bill:",C)

        elif (A==3):
            DD=int(input("how many eggbuffs:"))
            E=DD*eggbuffs
            print("Your Egg Buffs Bill:",E)

        elif (A==4):
            MM=int(input("how many mushbuffs:"))
            F=MM*mushroombuffs
            print("Your Mushroombuffs Bill:",F)

        elif (A==5):
            VV=int(input("how many veg buffs:"))
            VE=VV*vegbuffs
            print("Your Veg Buffs Bill:",VE)

        elif (A==6):
            TOTAL_BILL=T+C+E+F+VE
            print("YOUR TOTAL BILL:",TOTAL_BILL)
            print("--------THANK YOU VISIT AGAIN-----")
            break

non_veg_foods=int(input("non-veg:"))
chickenbuffs=30
muttonbuffs=40
chickenroll=60
chickenlooypop=100
muttonsukka=150
chicken65=170

while True:
    if (non_veg_foods==2):
        print("1-chickenbuffs")
        print("2-muttonbuffs")
        print("3-chickenroll")
        print("4-chickenlooypop")
        print("5-muttonsukka")
        print("6-chicken65")
        print("TOTAL BILL=")
        B=int(input("which food you eats:"))

        if (B==1):
            z=int(input("how many chickenbuffs:"))
            Z=z*chickenbuffs
            print("your chickenbuffs bill:",Z)
        elif (B==2):
            y=int(input("how many muttonbuffs:"))
            Y=y*muttonbuffs
            print("your muttonbuffs bill:",Y)
        elif (B==3):
            x=int(input("how many chickenroll:"))
            X=x*chickenroll
            print("your chickenroll bill:",X)

        elif(B==4):
            h=int(input("how many muttonsukka:"))
            H=h*muttonsukka
            print("your muttonsukka bill:",H)
           
        elif (B==5):
            g=int(input("how many chicken65:"))
            G=g*chicken65
            print("your chicken65 bill:",G)

        elif (B==6):
            total=Z+Y+X+H+G
            print("TOTAL BILL",total)
            print(" -----------THANK YOU VISIT AGAIN----------------")
            break

'''            

            

           

        

            

            

        
    
        
    





























































        
            


        

