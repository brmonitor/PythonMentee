# Python Mentee - Level 2 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 5 - Create a Python function that accepts any number of positional and keyword arguments,
#       and that prints them back to the user.
#       Your output should indicate which values were provided as positional arguments,
#       and which were provided as keyword arguments.


def show_its_args_and_kwargs(*args, **kwargs):
    print(f"The args : {args}")
    print(f"The kwargs : {kwargs} \n")


if __name__ == '__main__':
    show_its_args_and_kwargs(3, 5)
    show_its_args_and_kwargs(name='Fred', surname='Red')
    show_its_args_and_kwargs(3, 5, name='Fred', surname='Red')
