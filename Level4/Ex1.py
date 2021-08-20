# Python Mentee - Level 4 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 1 - Write a Python regex function to find sequences of lowercase letters joined with an underscore.

from re import findall


def low_seq(text):
    return findall('[a-z]_[a-z]', text)


if __name__ == '__main__':
    test = '  a_ab_c  A-Ad_e  z_z y_w  '
    print(low_seq(test))
