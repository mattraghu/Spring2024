import datetime

def date_arithmetic():
    date1_1 = datetime.date(2021, 2, 27)
    date2_1 = date1_1 + datetime.timedelta(days=3)

    date1_2 = datetime.date(2020, 2, 27)
    date2_2 = date1_2 + datetime.timedelta(days=3)

    days_passed = datetime.date(2021, 2, 1) - datetime.date(2020, 9, 30)


    return (date2_1, date2_2, days_passed.days)

print(date_arithmetic())