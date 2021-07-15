from Calculation import *
from PrevMonthAmount import *
def FileWrite(Rb,name,amount,b):
    IncomeMoney="0"
    ExpenseMoney="0"
    TotalSavings="0"
    try:
        # Reading the file
        a=open(f"Database/Datas/{b}","r")
        datas=a.readlines()
        a.close()

        # Write the file
        a=open(f"Database/Datas/{b}","w")
        incomeList=datas[0].replace("[","").replace("]","").replace("'","").replace(",","").split()
        expenseList=datas[1].replace("[","").replace("]","").replace("'","").replace(",","").split()
        if(Rb=="1"):
            incomeList.append(name)
            incomeList.append(amount)
        else:
            expenseList.append(name)
            expenseList.append(amount)
        
        # Claculation Function
        in_amount,ex_amount,t_amount=Savings(incomeList,expenseList)
        IncomeMoney=in_amount
        ExpenseMoney=ex_amount
        TotalSavings=t_amount
        income=str(incomeList)
        expense=str(expenseList)

        a.write(income)
        a.write("\n")
        a.write(expense)
        a.write("\n")
        a.write(IncomeMoney)
        a.write("\n")
        a.write(ExpenseMoney)
        a.write("\n")
        a.write(TotalSavings)
        a.close()
    except FileNotFoundError:
        prevAmount=prevMonthAmount()
        incomes=[]
        expenses=[]   
        incomes.append("LastMonthSavings")     
        incomes.append(prevAmount)     
        # if File is not available
        a=open(f"Database/Datas/{b}","w")
        if(Rb=="1"):
            incomes.append(name)
            incomes.append(amount)
        else:
            expenses.append(name)
            expenses.append(amount)

        # Calculation Function
        in_amount,ex_amount,t_amount=Savings(incomes,expenses)

        IncomeMoney=in_amount
        ExpenseMoney=ex_amount
        TotalSavings=t_amount
        
        income=str(incomes)
        expense=str(expenses)

        a.write(income)
        a.write("\n")
        a.write(expense)
        a.write("\n")
        a.write(IncomeMoney)
        a.write("\n")
        a.write(ExpenseMoney)
        a.write("\n")
        a.write(TotalSavings)
        a.close()

def FileRead(month):
    a=open(f"Database/Datas/{month}","r+")
    datas=a.readlines()
    incomeList=datas[0].replace("[","").replace("]","").replace("'","").replace(",","").split()
    expenseList=datas[1].replace("[","").replace("]","").replace("'","").replace(",","").split()
    a.close()
    return incomeList,expenseList,datas[2].split("\n")[0],datas[3].split("\n")[0],datas[4].split("\n")[0]