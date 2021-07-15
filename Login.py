from tkinter import *
from Database.passcode.UseridAndPassword import *
from Home import *
def App():
    # Creating Root window
    root=Tk()
    root.configure(bg="yellow")
    root.title("Harinivash")
    # Minimum size
    root.minsize(500,500)
    # Maximum size
    name=StringVar()
    password=StringVar()

    def Login():
        username=name.get()
        passcode=password.get()
        if(username in User_id_password and User_id_password[username]==passcode):
            root.destroy()
            Home()
        elif(username=="" or passcode==""):
            wrong.place_forget()
            empty.place(x=100,y=320)
        else:
            empty.place_forget()
            wrong.place(x=100,y=320)
        name.set("")
        password.set("")
    def remove(event):
        wrong.place_forget()
        empty.place_forget()

    empty = Label(root,text=" name or password is empty",font=50,fg="red",bg="yellow")
    wrong = Label(root,text=" name or password is wrong",font=50,fg="red",bg="yellow")
    # Login Heading Label
    Label(text="Login",font=20,bg="yellow").place(x=210,y=170)
    # UserName Label
    Label(text="Username",font=18,bg="yellow").place(x=100,y=200)
    # Username Input box
    nameEntry=Entry(root,width=25,textvariable=name,fg="#a00").place(x=210,y=205)
    
    # Password Label
    Label(text="Password",font=18,bg="yellow").place(x=100,y=230)
    # Password Input box
    PasswordEntry=Entry(root,width=25,textvariable=password,show="*").place(x=210,y=235)
    # Login button
    btn=Button(root,text="Login",font=20,bg="Blue",fg="white",command=Login).place(x=230,y=270)
    root.resizable(0,0)
    root.bind("<Key>",remove)
    root.bind("<Button-1>",remove)
    root.bind("<Button-2>",remove)
    root.bind("<Button-3>",remove)
    mainloop()