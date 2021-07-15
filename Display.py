from tkinter import *
from File import *
def Display(month): 
    incomeList,expenseList,incomeTotal,expenseTotal,totalSavings=FileRead(month) 
    This_Month=Tk()
    This_Month.title("Harinivash")
    This_Month.configure(bg="yellow")
    This_Month.minsize(700,700)
    This_Month.resizable(0,0)
    v=Scrollbar(This_Month,orient='vertical')

    income=Text(This_Month, width = 15, height = 10,bg="yellow",font=5, wrap = NONE,yscrollcommand = v.set)
    expense=Text(This_Month, width = 15, height = 10,bg="yellow",font=5,wrap = NONE,yscrollcommand = v.set)

    v.pack(side = RIGHT, fill = "y")

    Label(This_Month,text=month.split(".txt")[0]+" Savings ",bg="yellow",font=20).pack()
    Label(This_Month,text="Income",bg="yellow",font=20,fg="Green").pack()
    
    # Displaying Income
    for i in range(len(incomeList)):
        if(i%2==0):
            income.insert(END,incomeList[i]+"\t\t\t")
        else:
            income.insert(END,incomeList[i]+"\n")
    income.pack(side=TOP, fill="x")
    v.config(command=income.yview)
    Label(This_Month,text=f"Total income  = {incomeTotal} Rs",bg="yellow",font=10).pack()
    
    Label(This_Month,text="Expense",bg="yellow",fg="Red",font=20).pack()
    for i in range(len(expenseList)):
        if(i%2==0):
            expense.insert(END,expenseList[i]+"\t\t\t")
        else:
            expense.insert(END,expenseList[i]+"\n")
    expense.pack(side=TOP, fill="x")
    v.config(command=expense.yview)
    Label(This_Month,text=f"Total expense = {expenseTotal} Rs",bg="yellow",font=10).pack()

    Label(This_Month,text=f"Total Savings Remaing = ",bg="yellow",font=10).place(x=260,y=613)

    if (float(totalSavings)>0):
        color="Green"
    else:
        color="Red"
    Label(This_Month,text=f"{totalSavings} Rs",bg="yellow",font=10,fg=color).place(x=450,y=613)
