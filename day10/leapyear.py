
month=int(input("enter month"))
year=int(input("enter year"))
def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
def days_in_month(year,month):
    """hello world
    how about that?
    return""" 
    month_days=[31,28,31,30,31,30,31,30,31,30,29,31]
    if is_leap(year) and month ==2:
        return 29
    return month_days[month -1]


is_leap(year)
days=days_in_month(year,month)
print(days)