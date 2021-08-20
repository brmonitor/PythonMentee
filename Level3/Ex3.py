# Python Mentee - Level 3 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 3 - Write a Python program that asks the user for their birth date and prints
#       the user’s current age in years, months, and days.
#       Sample output: You are 25 years, 4 months, and 22 days old

from datetime import datetime
from dateutil.relativedelta import relativedelta


def time_amount(time_unit, countdown):
    t = getattr(countdown, time_unit)
    return f"{t} {time_unit}" if t != 0 else ""


def age_ymd(dat):
    time_units = ["years", "months", "days"]
    dt_start = datetime.strptime(dat, '%d/%m/%Y')
    age_ymd = relativedelta(datetime.now(), dt_start)
    output = (t for tu in time_units if (t := time_amount(tu, age_ymd)))

    print('You are', ", ".join(output), 'old') 
    

if __name__ == '__main__':
    birthdate = input('Please enter your birthday (dd/mm/yyyy) : ')
    age_ymd(birthdate)
