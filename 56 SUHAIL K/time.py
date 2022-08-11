from datetime import date, timedelta
def sub(date1):
    dt = date1 - timedelta(5)
    return dt
date1 = date(2018, 12, 13)
print(sub(date1))
