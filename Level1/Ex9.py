# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 9 - Write a Python function to merge two dictionaries.

def merge_2_dic(d1, d2):
    d1.update(d2)
    print(d1)


if __name__ == '__main__':
    d1 = {0: 0, 1: 1, 2: 2}
    d2 = {0: 0, 3: 3, 4: 4}
    merge_2_dic(d1, d2)
