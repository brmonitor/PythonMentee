# Python Mentee - Level 3 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 2 - Write a Python program to display the current date and time.
#       Sample Output :
#           Current date and time : 2014-07-05 14:34:14

from datetime import datetime
from time import time

def human_time(t):  # from Level 2   Exercise 2
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

def date_time_now():
    print(str(datetime.now())[:-7])
    # other solution
    print(human_time(time()))
    # another solution
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    date_time_now()
