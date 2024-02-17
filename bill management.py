from tkinter import *

root = Tk()
root.geometry('1050x580')
root.title('BILL MANAGEMENT')
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_cookies.delete(0,END)
    entry_Tea.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Juice.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_Eggs.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except: a1=0

    try:a2=int(cookies.get())
    except: a2=0

    try:a3=int(Tea.get())
    except: a3=0

    try:a4=int(Coffee.get())
    except: a4=0

    try:a5=int(Juice.get())
    except: a5=0
    
    try:a6=int(pancakes.get())
    except: a6=0

    try:a7=int(Eggs.get())
    except: a7=0

#define cost of each item per quantity
    c1=40*a1
    c2=30*a2
    c3=10*a3
    c4=15*a4
    c5=30*a5
    c6=15*a6
    c7=7*a7

    lbl_total=Label(f2,font=('aria',20,'bold'),text='Total',width=16,fg='lightyellow',bg='black')
    lbl_total.place(x=0,y=60)

    entry_total=Entry(f2,font=(aria,20,'bold'),textVarlabel=Total_bill,bd=6,width=15,bg='lightgreen')
    entry_total.place(x=20,y=250)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill='Rs.',str('%.2f' %totalcost)
    Total_bill.set(string_bill)

Label(text="BILL MANAGEMENT",bg='black',fg='white',font=('calibari',33),width='300',height='2').pack()


 #MENU CARD
f=Frame(root,bg='lightgreen',highlightbackground='black',highlightthickness=2,width=330,height=400)
f.place(x=10,y=160)

Label(f,text='Menu',font=('Gabriola',40,'bold'),fg='black',bg='lightgreen').place(x=80,y=2)

Label(f,font=('lucida calligraphy',15,'bold'),text='Dosa..........Rs.40/plate',fg='black',bg='lightgreen').place(x=10,y=80)
Label(f,font=('lucida calligraphy',15,'bold'),text='Cookies..........Rs.30/plate',fg='black',bg='lightgreen').place(x=10,y=110)
Label(f,font=('lucida calligraphy',15,'bold'),text='Tea..........Rs.10/cup',fg='black',bg='lightgreen').place(x=10,y=140)
Label(f,font=('lucida calligraphy',15,'bold'),text='Coffee..........Rs.15/cup',fg='black',bg='lightgreen').place(x=10,y=170)
Label(f,font=('lucida calligraphy',15,'bold'),text='Juice..........Rs.30/glass',fg='black',bg='lightgreen').place(x=10,y=200)
Label(f,font=('lucida calligraphy',15,'bold'),text='pancakes..........Rs.15/pack',fg='black',bg='lightgreen').place(x=10,y=230)
Label(f,font=('lucida calligraphy',15,'bold'),text='Eggs..........Rs.7/egg',fg='black',bg='lightgreen').place(x=10,y=260)

#Bill
f2=Frame(root,bg='lightyellow',highlightbackground='black',highlightthickness=1,width=310,height=370)
f2.place(x=720,y=160)

Bill=Label(f2,text="Bill",font=("calibri",20),bg='lightyellow')
Bill.place(150,y=20)

#ENTRY WORK
f1=Frame(root,bd=5,height=900,width=280,relief=RAISED)
f1.place(x=350,y=160)

dosa=StringVar()
cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
pancakes=StringVar()
Eggs=StringVar()
Total_bill=StringVar()

#Label

lbl_dosa=Label(f1,font=('aria',20,'bold'),text='Dosa',width=12,fg='blue')
lbl_cookies=Label(f1,font=('aria',20,'bold'),text='Cookies',width=12,fg='blue')
lbl_tea=Label(f1,font=('aria',20,'bold'),text='Tea',width=12,fg='blue')
lbl_coffee=Label(f1,font=('aria',20,'bold'),text='Coffee',width=12,fg='blue')
lbl_juice=Label(f1,font=('aria',20,'bold'),text='Juice',width=12,fg='blue')
lbl_pancakes=Label(f1,font=('aria',20,'bold'),text='pancakes',width=12,fg='blue')
lbl_eggs=Label(f1,font=('aria',20,'bold'),text='Eggs',width=12,fg='blue')

lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_tea.grid(row=3,column=0)
lbl_coffee.grid(row=4,column=0)
lbl_juice.grid(row=5,column=0)
lbl_pancakes.grid(row=6,column=0)
lbl_eggs.grid(row=7,column=0)



#Entry
entry_dosa=Entry(f1,font=('aria',20,'bold'),textvariable=dosa,bd=6,width=8,bg='lightpink')
entry_cookies=Entry(f1,font=('aria',20,'bold'),textvariable=cookies,bd=6,width=8,bg='lightpink')
entry_Tea=Entry(f1,font=('aria',20,'bold'),textvariable=Tea,bd=6,width=8,bg='lightpink')
entry_Coffee=Entry(f1,font=('aria',20,'bold'),textvariable=Coffee,bd=6,width=8,bg='lightpink')
entry_Juice=Entry(f1,font=('aria',20,'bold'),textvariable=Juice,bd=6,width=8,bg='lightpink')
entry_pancakes=Entry(f1,font=('aria',20,'bold'),textvariable=pancakes,bd=6,width=8,bg='lightpink')
entry_Eggs=Entry(f1,font=('aria',20,'bold'),textvariable=Eggs,bd=6,width=8,bg='lightpink')

entry_dosa.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_Tea.grid(row=3,column=1)
entry_Coffee.grid(row=4,column=1)
entry_Juice.grid(row=5,column=1)
entry_pancakes.grid(row=6,column=1)
entry_Eggs.grid(row=7,column=1)


#Button

btn_reset=Button(f1,bd=5,fg='black',bg='lightblue',font=('arie1',16,'bold'),width=10,text='Reset',command=Reset)
btn_reset.grid(row=8,column=0)


btn_total=Button(f1,bd=5,fg='black',bg='green',font=('arie1',16,'bold'),width=10,text='Total',command=Total)
btn_total.grid(row=8,column=1)


root.mainloop()



























