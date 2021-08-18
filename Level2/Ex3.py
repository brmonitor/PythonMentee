# Python Mentee - Level 2 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 3 - Write a Python program that takes user input and runs it as a command using the os module.

from os import system


def user_comm(comm):
    print(f'*** Command entered by the user : {comm}  ***\n')
    ret = system(comm)
    print(f'\n*** Command entered by the user ran with exit code : {ret} \n')


if __name__ == '__main__':
    c = input('Type the command that you want to be executed on the Operating System : ')
    user_comm(c)
