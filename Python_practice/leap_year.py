#Number of days per month.First value the place holder for indexing purposes
month_days = [0,31,28,30,31,31,30,29,30,31,30]
def is_leap(year):
    """Return true for leap year and False for Non leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_of_month(year,month):
    """Return the number of days in that month and in that year"""
    if not month <= 12:
        return "Invalid month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]   

#print(is_leap(2020))   
print(days_of_month(2017,2))         