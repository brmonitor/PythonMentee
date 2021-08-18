# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 7 - Write a Python function to remove duplicates from a list

def list_no_duplicates(l):
    s = set(l)
    print(list(s))


if __name__ == '__main__':
    l = [1,2,3,4,1,1,2,5,6]
    list_no_duplicates(l)
