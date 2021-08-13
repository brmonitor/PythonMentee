# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 10 - Write a Python program that iterates through integers from 1 to 100 and prints them.
#       For integers that are multiples of three, print "Fizz" instead of the number.
#       For integers that are multiples of five, print "Buzz".
#       For integers which are multiples of both three and five print, "FizzBuzz".

def rangnum_div_3_or_5(n):
    for i in range(1, n+1):
        p = i
        if i % 3 == 0 and i % 5 == 0:
            p = 'FizzBuzz'
        elif i % 3 == 0:
            p = 'Fizz'
        elif i % 5 == 0:
            p = 'Buzz'

        print(p)


if __name__ == '__main__':
    rangnum_div_3_or_5(100)
