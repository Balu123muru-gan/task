from tkinter import*
import datetime as dt
from tkinter import ttk
loki=Tk()


loki.title("Hotel Management System")

h=loki.winfo_screenheight()
w=loki.winfo_screenwidth()
loki.configure(height=h,width=w,bg='#ccd5ae')

bg=PhotoImage(file='Royal.png')
lbroyal=Label(loki,image=bg)
lbroyal.place(x=0,y=0)

bg2=PhotoImage(file='hotel.png')
lb2=Label(loki,image=bg2)
lb2.place(x=180,y=0)


lb3=Label(loki,text=" ROYAL RESIDENCY ",font=('Times new roman',30,'bold'),bg='#02c39a',fg='white',width=60)
lb3.pack(pady=155)

date=dt.datetime.now()

lbtime=Label(loki,text=f"{date:%H:%M:%S  %p}",font=('prestige elite std',20,'bold'),bg='#02c39a',fg='white')
lbtime.place(x=10,y=160)

       
                              
lbcd=Label(loki,text="Customer Details",font=('times new roman',20,'bold'),bg='#ccd5ae')
lbcd.place(x=0,y=210)

lbreg=Label(loki,text="Reg Number",font=('prestige elite std',20,'bold'),bg='#ccd5ae')
lbreg.place(x=0,y=270)

lbname=Label(loki,text="Name",font=('prestige elite std',20,'bold'),bg='#ccd5ae')
lbname.place(x=0,y=320)

lbgender=Label(loki,text="Gender",font=('prestige elite std',20,'bold'),bg='#ccd5ae')
lbgender.place(x=0,y=370)

lbmob=Label(loki,text="Mobile",font=('prestige elite std',20,'bold'),bg='#ccd5ae')
lbmob.place(x=0,y=420)

lbemail=Label(loki,text="Email",font=('prestige elite std',20,'bold'),bg='#ccd5ae')
lbemail.place(x=0,y=470)

lbproof=Label(loki,text="Proof Type",font=('prestige elite std',20,'bold'),bg='#ccd5ae')
lbproof.place(x=0,y=520)

lbid=Label(loki,text="ID Proof",font=('prestige elite std',20,'bold'),bg='#ccd5ae')
lbid.place(x=0,y=570)

lbaddress=Label(loki,text="Address",font=('prestige elite std',20,'bold'),bg='#ccd5ae')
lbaddress.place(x=0,y=620)



tb1=Entry(font=('prestige elite std',20,'bold'),width=15)
tb1.place(x=190,y=270)

tb2=Entry(font=('prestige elite std',20,'bold'),width=15)
tb2.place(x=190,y=320)

tb3=Entry(font=('prestige elite std',20,'bold'),width=15)
tb3.place(x=190,y=420)

tb4=Entry(font=('prestige elite std',20,'bold'),width=15)
tb4.place(x=190,y=470)

tb5=Entry(font=('prestige elite std',20,'bold'),width=15)
tb5.place(x=190,y=570)

tb6=Text(font=('prestige elite std',20,'bold'),width=15,height=2)
tb6.place(x=190,y=620)

combogender=ttk.Combobox(loki,font=("prestige elite std",20),width=14,values=("Male","Famale","Transgender"))
combogender.place(x=190,y=370)

'''radio=IntVar()

radbut1=Radiobutton(loki,text="Male",variable=radio,height=1,width=4,value='Male',
                    font=('prestige elite std',18,'bold'),bg='#ccd5ae')
radbut1.place(x=190,y=370)

radbut2=Radiobutton(loki,text="Female",variable=radio,height=1,width=6,value='Female',
                    font=('prestige elite std',18,'bold'),bg='#ccd5ae')
radbut2.place(x=300,y=370)'''


comboproof=ttk.Combobox(loki,font=("prestige elite std",20),width=14,values=("Aadhaar card","PAN card","Pass port","Driving License"))
comboproof.place(x=190,y=520)

tbsearch=Entry(font=('prestige elite std',18,'bold'),width=25)
tbsearch.place(x=750,y=420)



tree=ttk.Treeview()
style=ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading",background="red",foreground="white",rowheight=60)
style.configure("Treeview",fieldbackground='#657483')
style.map("Treeview",background=[('selected','blue')])
tree['columns']=('r','n','g','m','e','p','i','a')
tree.column('#0',width=0,stretch=NO)
tree.column('r',width=40)
tree.column('n',width=120)
tree.column('g',width=80)
tree.column('m',width=110)
tree.column('e',width=140)
tree.column('p',width=120)
tree.column('i',width=120)
tree.column('a',width=185)

tree.heading('r',text='R.no')
tree.heading('n',text='Name')
tree.heading('g',text='Gender')
tree.heading('m',text='Mobile')
tree.heading('e',text='Email')
tree.heading('p',text='Proof Type')
tree.heading('i',text='ID Proof')
tree.heading('a',text='Address')

tree.place(x=445,y=465)


##def show():
##    import tkinter as tk
##    from tkinter import ttk
##    leo=Tk()
##
##    leo.title("Hotel Management System")
##    leo.geometry("1200x400")
##    leo.configure(bg='#ccd5ae')
##
##    tb=Entry(loki,font=('prestige elite std',18,'bold'),width=25)
##    tb.pack(pady=40)
##    tree=ttk.Treeview()
##    style=ttk.Style()
##    style.theme_use('clam')
##    style.configure("Treeview.Heading",background="red",foreground="black",rowheight=60)
##    style.configure("Treeview",fieldbackground='#657483')
##    style.map("Treeview",background=[('selected','red')])
##    tree['columns']=('r','n','g','m','e','p','i','a')
##    tree.column('#0',width=0,stretch=NO)
##    tree.column('r',width=90)
##    tree.column('n',width=130)
##    tree.column('g',width=100)
##    tree.column('m',width=150)
##    tree.column('e',width=150)
##    tree.column('p',width=150)
##    tree.column('i',width=150)
##    tree.column('a',width=275)
##
##    tree.heading('r',text='Reg Number')
##    tree.heading('n',text='Name')
##    tree.heading('g',text='Gender')
##    tree.heading('m',text='Mobile')
##    tree.heading('e',text='Email')
##    tree.heading('p',text='Proof Type')
##    tree.heading('i',text='ID Proof')
##    tree.heading('a',text='Address')
##
##    tree.place(x=0,y=150)

##but=Button(loki,text="SEARCH",font=('times new roman',10,'bold'),bg='#ffbe0b',border=10,cursor="hand2",width=15,)
##but.place(x=530,y=90)

global count
count=1

def save():
    global count
    tree.insert(parent='',index='end',iid=count,values=(tb1.get(),tb2.get(),combogender.get(),tb3.get(),tb4.get(),
                                                        comboproof.get(),tb5.get(),tb6.get(1.0,'end-1c')))
    count+=1


def select():
    tb1.delete(0,'end')
    tb2.delete(0,'end')
    tb3.delete(0,'end')
    tb4.delete(0,'end')
    tb5.delete(0,'end')
    tb6.delete(1.0,'end')
    combogender.delete(0,'end')
    comboproof.delete(0,'end')
    
    x=tree.selection()
    values=tree.item(x,'values')
    
    tb1.insert(0,values[0])
    tb2.insert(0,values[1])
    combogender.insert(0,values[2])
    tb3.insert(0,values[3])
    tb4.insert(0,values[4])
    comboproof.insert(0,values[5])
    tb5.insert(0,values[6])
    tb6.insert(1.0,values[7])


def update():
    sel=tree.focus()
    values=tree.item(sel,values=(tb1.get(),tb2.get(),combogender.get(),tb3.get(),tb4.get(),comboproof.get(),
                                 tb5.get(),tb6.get(1.0,'end-1c')))

    tb1.delete(0,'end')
    tb2.delete(0,'end')
    tb3.delete(0,'end')
    tb4.delete(0,'end')
    tb5.delete(0,'end')
    tb6.delete(1.0,'end')
    combogender.delete(0,'end')
    comboproof.delete(0,'end')


def clear():
     tb1.delete(0,'end')
     tb2.delete(0,'end')
     tb3.delete(0,'end')
     tb4.delete(0,'end')
     tb5.delete(0,'end')
     tb6.delete(1.0,'end')
     combogender.delete(0,'end')
     comboproof.delete(0,'end')
    


def delete():
    for i in tree.focus():
        tree.delete(i)

#def search():
    
    

but1=Button(loki,text="SAVE",font=('times new roman',15,'bold'),width=9,bg='#7209b7',fg='white',border=10,
            cursor="hand2",command=save)
but1.place(x=550,y=330)

but2=Button(loki,text="UPDATE",font=('times new roman',15,'bold'),width=9,bg='#7209b7',fg='white',border=10,
            cursor="hand2",command=update)
but2.place(x=700,y=330)

but3=Button(loki,text="DELETE",font=('times new roman',15,'bold'),width=9,bg='#7209b7',fg='white',border=10,
            cursor="hand2",command=delete)
but3.place(x=850,y=330)

but4=Button(loki,text="CLEAR",font=('times new roman',15,'bold'),width=9,bg='#7209b7',fg='white',border=10,
            cursor="hand2",command=clear)
but4.place(x=1000,y=330)

but5=Button(loki,text="SELECT",font=('times new roman',15,'bold'),width=9,bg='#7209b7',fg='white',border=10,
            cursor="hand2",command=select)
but5.place(x=1150,y=330)


but6=Button(loki,text="SEARCH",font=('times new roman',10,'bold'),width=12,bg='#03071e',fg='white',border=7,
            cursor="hand2",command=select)
but6.place(x=1110,y=420)








loki.mainloop()
