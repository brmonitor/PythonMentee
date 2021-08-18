# Python Mentee - Level 2 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 4 - Create a Python function that accepts any number of numbers
#       as positional arguments and prints the sum of those numbers.


def sum_any(*nums):
    summ = 0
    for n in nums:
        summ += n
    print(f"Sum of {nums} = ", summ)


if __name__ == '__main__':
    sum_any(3, 5)
    sum_any(4, 5, 6, 7)
    sum_any(1, 2, 3, 5, 6)
