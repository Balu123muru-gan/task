class slot:
    def getslot(self):
        self.date=int(input())
        self.slotid=int(input())
        self.noseats=int(input())
        
class student:
    def getstud(self):
        self.sid=int(input())
        self.cutoff=int(input())
        self.age=int(input())
        self.hsc=int(input())
        self.sslc=int(input())
        self.cdate=0
        self.cslotid=0
 #=======================input  start =============       
noslots=int(input()) 
slots=[] #0 1 2 3 4
for _ in range(noslots):
    s=slot()
    s.getslot()
    slots.append(s)
    
nostudents=int(input())
students=[]
for _ in range(nostudents):
    s=student()  
    s.getstud()
    students.append(s)
    fsid=int(input())
#==================== input end ==============
    
for i in range(nostudents):
    print(students[i].sid,students[i].cutoff,students[i].age,students[i].hsc,students[i].sslc)


for i in range(nostudents):
    for j in range(i+1,nostudents):
        if students[i].cutoff<students[j].cutoff:
            temp=students[i]
            students[i]=students[j]
            students[j]=temp

#for i in range(nostudents):
 #   print(students[i].sid,students[i].cutoff,students[i].age,students[i].hsc,students[i].sslc)

for i in range(nostudents):
    for j in range(i+1,nostudents):
        if students[i].cutoff==students[j].cutoff:
            if students[i].age<students[j].age:
                temp=students[i]
                students[i]=students[j]
                students[j]=temp

#for i in range(nostudents):
  #  print(students[i].sid,students[i].cutoff,students[i].age,students[i].hsc,students[i].sslc)

for i in range(nostudents):
    for j in range(i+1,nostudents):
        if students[i].cutoff==students[j].cutoff:
            if students[i].age==students[j].age:
                if students[i].hsc<students[j].hsc:
                    temp=students[i]
                    students[i]=students[j]
                    students[j]=temp

                    
#for i in range(nostudents):
  #  print(students[i].sid,students[i].cutoff,students[i].age,students[i].hsc,students[i].sslc)

for i in range(nostudents):
    for j in range(i+1,nostudents):
        if students[i].cutoff==students[j].cutoff:
            if students[i].age==students[j].age:
                if students[i].hsc==students[j].hsc:
                    if students[i].sslc<students[j].sslc:
                        temp=students[i]
                        students[i]=students[j]
                        students[j]=temp

for i in range(nostudents):
    print(students[i].sid,students[i].cutoff,students[i].age,students[i].hsc,students[i].sslc)                        

totseats=0   
for i in range(len(slots)):
    totseats=totseats+slots[i].noseats
    print(slots[i].date,slots[i].slotid,slots[i].noseats)
    print("totalseata:",totseats)

a=0
if nostudents<=totseats:
    for i in range(len(slots)):
        for j in range(slots[i].noseats):
            students[a].cdate=slots[i].date
            students[a].cslotid=slots[i].slotid
            a=a+1
            if a==nostudents:
                break
            if a==nostudents:
                break

for i in range(nostudent):
    print(students[i].sid,students[i].cutoff,students[i].age,students[i].hsc,students[i].sslc,students[i].cdate,students[i].cslotid )

for i in  range(nostudents):
    if fsid==students[i].sid:
        print(students[i].cdate,"|",fsid,"|",students[i].cslotid,sep=" ")
        break
    
            

            


























    
