# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 1 - Write a Python program to test whether a passed letter is a vowel or not.

def isItVowel(c):
    if c.lower() in 'aeiou':
        print(f'{c} is a vowel')
    else:
        print(f'{c} is NOT a vowel')


if __name__ == '__main__':
    while True:
        s = input('Type any letter on the keyboard : ')
        isItVowel(s[0])
