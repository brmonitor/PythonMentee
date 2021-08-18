# Python Mentee - Level 2 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 1 - Write a Python program to scan a specified directory and identify the sub directories and files.

from os import listdir

def lisDir(path):
    dir_list = listdir(path)
    print(f"Files and directories in {path} :")
    for entry in dir_list:
        print(entry)


if __name__ == '__main__':
    while True:
        d = input('Type the directory that you want to scan : ')
        lisDir(d)
