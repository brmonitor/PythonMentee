# Python Mentee - Level 3 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 1 - Write a Python program to count the number of strings where the string length is 2 or more
#       and the first and last character are the same from a given list of strings.
#           Sample List : ['abc', 'xyz', 'aba', '1221']
#           Expected Result : 2

def list_check_equal_first_and_last_char(lis):
    count = 0
    for s in lis:
        if len(s)>1 and s[0]==s[-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    list_check_equal_first_and_last_char(['abc', 'xyz', 'aba', '1221'])
    list_check_equal_first_and_last_char(['aa', 'xyx', 'bb', '1221'])

