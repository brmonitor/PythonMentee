# Python Mentee - Level 4 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 3 - Create a decorator that makes sure that all function arguments where it's applied will match the regex
#       on the regex exercise above.

from re import findall, search


def my_decorator(func):
    def wrapper(text):
        pattern = '[a-z]_[a-z]'
        if search(pattern, text):
            print(f'The text ({text}) matches the pattern ({pattern}) : ({func(text)})')
        else:
            print(f'*** The text ({text}) does not match the pattern ({pattern}) ***')
    return wrapper


@my_decorator
def low_seq(text):
    return findall('[a-z]_[a-z]', text)


if __name__ == '__main__':
    low_seq('a_z 1_2 x_y')
    low_seq('az')

