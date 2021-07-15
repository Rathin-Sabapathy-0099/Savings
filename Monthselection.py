from tkinter import *
from tkinter.ttk import *
from Display import *
# import hashlib

def Monthselection(a):
    month=Tk()
    # Find Files for previous Datas
    b=[]
    for i in a:
        b.append(i.split(".txt")[0])
    # warn label
    warn=Label(month,text="No month selected",bg="yellow",fg="red",font=5)

    # Selectiog the month to display the data
    def Find():
        value = combobox.get()
        # //sha256 = hashlib.sha256(value.encode())//#
        if(value!=""):
            month.destroy()
            # Displaying the data dor selected month
            Display(value+".txt")
        else:
            warn.place(x=50,y=200)
    def Remove(event):
        warn.place_forget()
    month.title("Harinivash")
    month.configure(bg="yellow")
    month.minsize(300,300)
    month.resizable(0,0)
    Label(month,text="Select the month to find the data ",font=20,bg="yellow").pack()

    MONTH=StringVar()
    style = Style()
    style.map('TCombobox', fieldbackground=[('readonly','white')])
    style.map('TCombobox', selectbackground=[('readonly', 'white')])
    style.map('TCombobox', selectforeground=[('readonly', 'black')])

    combobox = Combobox(month,textvariable=MONTH,height=15,justify='left',width=21,state="readonly")
    combobox['values'] = (b)
    combobox.place(x=80,y=50)
    combobox.bind('<Button-1>', Remove)
    month.bind("<Button-1>",Remove)
    month.bind("<Button-2>",Remove)
    month.bind("<Button-3>",Remove)
    combobox.current()
    Button(month,text="Find",command=Find,bg="blue",fg="white",font=20).place(x=120,y=150)