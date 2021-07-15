from tkinter import *
from Display import *
from Date import getDate
from Monthselection import *
from File import *
import os

def Home():
    month,year=getDate()
    Home=Tk()
    Home.configure(bg="yellow")
    Home.title("Harinivash")
    # Minimum size
    Home.minsize(500,500)
    # Maximum size
    Home.resizable(0,0)
    floatWarn=Label(Home,text="Don't Enter comma or anyother String except '.'",fg="red",bg="yellow",font=1)
    warnEmpty=Label(Home,text="Empty Values are not allowed 🤬",fg="red",bg="yellow",font=1)
    # Rb warn
    RbWarn=Label(Home,text="Select anyone from Type",fg="red",bg="yellow",font=1)
    def Input():
        if(name.get().replace(" ","")=="" or R1.get().replace(" ","")==""):
            RbWarn.place_forget()
            floatWarn.place_forget()
            warnEmpty.place(x=100,y=260)
        else:
            try :
                float(Rate.get())
                Rb=R1.get()
                # print(Rb)
                if(Rb=="-1"):
                    warnEmpty.place_forget()
                    floatWarn.place_forget()
                    RbWarn.place(x=150,y=260)
                else:
                    Amount=Rate.get()
                    nameStr=name.get()
                    name.set("")
                    Rate.set("")
                    R1.set("-1")
                    FileWrite(Rb,nameStr.replace(" ",""),Amount,f"{month}-{year}.txt")
            except ValueError:
                RbWarn.place_forget()
                warnEmpty.place_forget()
                floatWarn.place(x=50,y=260)

    def ThisMonthSavings():
        Display(f"{month}-{year}.txt")

    def AllMonthSavings():
        a=os.listdir("Database/Datas")
        Monthselection(a)

    # def help():
    #     print("How can I help you") 

    def remove(event):
        warnEmpty.place_forget()
        RbWarn.place_forget()
        floatWarn.place_forget()
    
    # Menu
    menubar=Menu(Home)
    # Menu options
    Savings=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Find",menu=Savings)
    Savings.add_command(label="This Month Savings",command=ThisMonthSavings)
    Savings.add_command(label="All Month Savings",command=AllMonthSavings)
    # Savings.add_command(label="Help",command=help)
    # displaying menubar
    Home.config(menu=menubar)
    # Label for Month
    Label(Home,text=f"{month}-{year}",font=20,fg="#f50",bg="yellow").pack()
    
    # tkinter Variable to store user values
    # Radio button Variable
    R1=StringVar(Home,"-1")

    # input box Variables
    name=StringVar()
    Rate=StringVar()
    
    # Label for Entry
    Label(Home,text="Enter the name",font=10,bg="yellow").place(x=0,y=45)
    Entry(Home,width=30,textvariable=name).place(x=150,y=50)

    Label(Home,text="Type",font=10,bg="yellow").place(x=0,y=100)
    X=150
    Y=100

    for text,value in {"Income":"1","Expense":"0"}.items():
        Radiobutton(Home,text=text,value=value,variable=R1,font=10,bg="yellow").place(x=X,y=Y)
        X=X+X
    
    Label(Home,text="Rate",font=10,bg="yellow").place(x=0,y=180)
    Entry(Home,width=30,textvariable=Rate).place(x=150,y=180)

    Button(Home,text="Submit",font=20,bg="Blue",fg="white",command=Input).place(x=200,y=220)

    # To Remove the warning messages on Key-Strokes
    Home.bind("<Key>",remove)
    Home.bind("<Button-1>",remove)
    Home.bind("<Button-2>",remove)
    Home.bind("<Button-3>",remove)