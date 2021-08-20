# Python Mentee - Level 3 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 6  - Write a python file with two functions: a function that receives a number and appends to a global variable list,
#       and another function that returns this list ordered.

lis = []


def append_global_list(n):
    lis.append(n)


def global_lis_sorted():
    lis.sort()
    return lis


if __name__ == '__main__':
    append_global_list(4)
    append_global_list(3)
    append_global_list(2)
    append_global_list(1)
    print('Unsorted global list : ', lis)
    print('Sorted global list   : ', global_lis_sorted())
