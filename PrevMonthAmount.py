import datetime
from Date import getDate

def prevMonthAmount():
    now = datetime.datetime.now()
    monthName,year = getDate()
    monthinteger = now.month-1
    month=datetime.date(int(year), monthinteger, 1).strftime('%b')
    try:
        prevMonthFile=open(f"Database/Datas/{month}-{year}.txt","r")
        datas=prevMonthFile.readlines()
        prevMonthFile.close()
        return datas[4].split("\n")[0]
    except:
        return "0"