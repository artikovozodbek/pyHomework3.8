from datetime import date

year = int(input("Year: "))
month = int(input("month: "))
day = int(input("day: "))

birthay_day = date(year, month, day)
today = date.today()

days_passed = today - birthay_day
print(days_passed.days)
