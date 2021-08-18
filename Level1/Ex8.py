# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 8 - Write a Python function to remove an item from a tuple.

def tuple_remove_item(tup, i):
    lis = list(tup)
    lis.remove(i)
    print(tuple(lis))


if __name__ == '__main__':
    tup = ('a', 'b', 'c')
    tuple_remove_item(tup, 'b')
