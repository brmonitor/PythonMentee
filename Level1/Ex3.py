# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 3 - Write a Python program that accepts a filename from the user and prints the filename’s extension.
#       Sample filename : abc.java
#       Output : java

def showExtension(filename):
    names = filename.split(sep='.')
    print(f'Its extension is : {names[1]}')


if __name__ == '__main__':
    while True:
        filename = input('Please type a filename with its extension : ')
        showExtension(filename)
