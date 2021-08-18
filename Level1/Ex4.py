# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 4 - Write a Python program to count the number of lines in a text file.

def line_count(fname):
    with open(fname, 'r') as f:
        count = len(f.readlines())
    print(f'This file has {count} lines')


if __name__ == '__main__':
    while True:
        name = input('Please type the text filename with its extension : ')
        line_count(name)
