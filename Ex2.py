# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 2 - Write a Python program that accepts the user's first and last name and prints them
#       in reverse order with a space between them.

def reverseName(name):
    names = name.split()
    print(f'In reverse order : {names[1]} {names[0]}')


if __name__ == '__main__':
    while True:
        name = input('Please type your first and last name : ')
        reverseName(name)
