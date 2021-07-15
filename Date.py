from datetime import date
def getDate():
    Todays_Date=date.today()
    return Todays_Date.strftime("%b"),str(Todays_Date.year)