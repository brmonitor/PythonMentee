# Python Mentee - Level 1 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 5 - Write a Python program to count the frequency of words in a text file.

def words_count(name):
    with open(name, 'r') as f:
        data = f.read()
        words = data.split()
        dic_words = dict()
        for w in words:
            if dic_words.get(w):
                dic_words[w] += 1
            else:
                dic_words.setdefault(w, 1)
        print('Frequency of words in this text file')
        print(dic_words)
        for k, v in dic_words.items():
            print(k, v)


if __name__ == '__main__':
    while True:
        name = input('Please type the text filename with its extension : ')
        words_count(name)
