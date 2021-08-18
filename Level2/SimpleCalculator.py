# Python Mentee - Level 2 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# The objective is to write an interactive calculator. User input is assumed to be a formula that consists of a number,
#   an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1).
#   Split user input and check whether the resulting list is valid:
#       _ If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#       _ Convert the 1st and 3rd input to a float. Handle any ValueError that occurs, and instead raise a FormulaError.
#       _ If the second input is not '+' or '-', again raise a FormulaError.

#   If the input is valid, perform the calculation and print out the result. The user is then prompted to provide
#       new input, and so on, until the user enters quit.

class FormulaError(Exception):
    pass


def simple_calc():
    while True:
        expression = input('Input a simple sum(+) or subtraction(-) between 2 numbers separated by white space (e.g. 1 + 1) : ')
        if expression == 'quit':
            print('Bye bye..')
            quit()
        e = expression.split()
        try:
            if len(e) != 3 or e[1] not in ('+', '-'):
                raise FormulaError
            else:
                #fin = float(eval(expression))
                print(f'{float(e[0])} {e[1]} {float(e[2])} = {float(eval(expression))}')
        except (FormulaError, ValueError):
            print("There is a FormulaError")
        print('Enter the word : quit to exit\n')


if __name__ == '__main__':
    simple_calc()
