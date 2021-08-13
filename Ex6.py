# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 6 - Write a Python program that takes an input string from the user and counts the frequency of characters in the string.
#       Sample String : google.com
#       Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def chars_count(word):
    chars = list(word)
    dic_chars = dict()
    for c in chars:
        if dic_chars.get(c):
            dic_chars[c] += 1
        else:
            dic_chars.setdefault(c, 1)
    print('Frequency of chars in this word/sentence')
    print(dic_chars)
    for k, v in dic_chars.items():
        print(k, v)


if __name__ == '__main__':
    while True:
        word = input('Please type any long word or sentence: ')
        chars_count(word)
