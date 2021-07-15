def Savings(income,expense):
    a=0
    incomeAmount=0.0
    expenseAmount=0.0
    for i in income:
        if(a%2==0):
            a+=1
        else:
            incomeAmount+=float(i)
            a+=1
    a=0
    for i in expense:
        if(a%2==0):
            a+=1
        else:
            expenseAmount+=float(i)
            a+=1
    totalSavings=incomeAmount-expenseAmount
    return str(incomeAmount),str(expenseAmount),str(totalSavings)