from datetime import date

def to_independence_day():
    today = date.today()
    year = today.year
    independence_day = date(year, 9, 1)

    if today > independence_day:
        independence_day = date(year+1, 9, 1)

        days_left = (independence_day - today).days
        return days_left
    
days_left = to_independence_day()
print(f"There are {days_left} days left until Independence Day")