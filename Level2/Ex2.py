# Python Mentee - Level 2 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 2 - Write a Python program to get the size, permissions*, owner*, device*, created,
#       last modified, and last accessed date time of a specified path.
#       * Unfortunately It is not so easy to have more info about these 3 : permissions*, owner*, device*

from datetime import datetime
from os import stat

def human_time(t):
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

def path_info(path):
    s = stat(path)

    print(f"\n Some info from path {path} :")
    print(f'    Size (bytes) : {s.st_size}')
    print(f'    Permissions  : {s.st_mode}')
    print(f'    Owner        : {s.st_uid}')
    print(f'    Device       : {s.st_dev}')
    print(f'    Created      : {human_time(s.st_ctime)}')
    print(f'    Modified     : {human_time(s.st_mtime)}')
    print(f'    Accessed     : {human_time(s.st_atime)}')
    print()

if __name__ == '__main__':
    while True:
        p = input('Type the path that you want to know more about : ')
        path_info(p)
