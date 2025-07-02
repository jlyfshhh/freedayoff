#!/usr/bin/env python3

import datetime

def nth_weekday_of_month(year, month, weekday, n):
    count = 0
    for day in range(1, 32):
        try:
            d = datetime.date(year, month, day)
        except ValueError:
            break
        if d.weekday() == weekday:
            count += 1
            if count == n:
                return d
    return None

def last_weekday_of_month(year, month, weekday):
    for day in range(31, 0, -1):
        try:
            d = datetime.date(year, month, day)
            if d.weekday() == weekday:
                return d
        except ValueError:
            continue
    return None

def compute_holidays(year):
    holidays = []

    fixed = [
        ("New Year's Day", datetime.date(year, 1, 1)),
        ("Juneteenth", datetime.date(year, 6, 19)),
        ("Independence Day", datetime.date(year, 7, 4)),
        ("Veterans Day", datetime.date(year, 11, 11)),
        ("Christmas Day", datetime.date(year, 12, 25))
    ]
    holidays.extend(fixed)

    holidays.append(("Martin Luther King Jr. Day", nth_weekday_of_month(year, 1, 0, 3)))
    holidays.append(("Presidents’ Day", nth_weekday_of_month(year, 2, 0, 3)))
    holidays.append(("Memorial Day", last_weekday_of_month(year, 5, 0)))
    holidays.append(("Labor Day", nth_weekday_of_month(year, 9, 0, 1)))
    holidays.append(("Columbus Day", nth_weekday_of_month(year, 10, 0, 2)))
    holidays.append(("Thanksgiving Day", nth_weekday_of_month(year, 11, 3, 4)))

    return sorted(holidays, key=lambda x: x[1])

def filter_weekday_holidays(holidays):
    return [(name, date) for name, date in holidays if date.weekday() < 5]

def find_next_holiday(holidays, today):
    for name, date in holidays:
        if date >= today:
            return name, date
    return None, None

def main():
    today = datetime.date.today()
    year = today.year

    holidays = compute_holidays(year)
    holidays = filter_weekday_holidays(holidays)

    name, date = find_next_holiday(holidays, today)

    if name is None:
        next_year = year + 1
        holidays = compute_holidays(next_year)
        holidays = filter_weekday_holidays(holidays)
        name, date = find_next_holiday(holidays, datetime.date(next_year, 1, 1))

    days_until = (date - today).days

    print("===============================")
    print(f"Name: {name}")
    print(f"Date: {date} ({date.strftime('%A')})")
    print(f"Days Until: {days_until}")
    print("===============================\n")

if __name__ == "__main__":
    main()