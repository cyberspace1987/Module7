#Generally put your doc string at the Top.
#When you have modified and filled out the below doc string
#delete this line and the 2 lines above it
"""
Program: basic_list.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
Write a python file basic_list.py and declare two functions make_list()
with pass and get_input() with pass (function not written keyword).
Function make_list() will eventually return a list of user input while get_input()
will get one input and return it
"""
user_list = []


def make_list(user_input):
    for i in range(3):  # loop
        try:

            user_input = int(input("Please enter a number"))  # asks for input.
        except ValueError:
            print("Enter a number")
        user_list.append(user_input)


def get_input(user_list):
    return ('return_value=' + str(user_list[1]))


if __name__ == '__main__':
    make_list([3, 5, 6])
    get_input(user_list)

