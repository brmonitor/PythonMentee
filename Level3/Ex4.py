# Python Mentee - Level 3 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 4  - Write a Python function using list comprehension that receives a list of words and
#       returns a list that contains:
#       _ The number of characters in each word if the word has 3 or more characters
#       _ The string “x” if the word has fewer than 3 characters


def convert_l(lis):
    out = []
    for w in lis:
        if len(w) >= 3:
            out.append(len(w))
        else:
            out.append('x')
    print(out)


def convert_l2(lis):
    print([len(w) if len(w) >= 3 else 'x' for w in lis])


if __name__ == '__main__':
    lista = ['abc', 'ab', '', 'abcd']
    convert_l(lista)
    convert_l2(lista)
