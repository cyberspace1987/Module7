"""
Program: basic_list.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
In Module7, copy basic_list.py and name it basic_list_exception.py.
Create test_basic_list_exception.py in the test_collections directory
and include the function that tests the list from test_basic_list.py.
Leave the function get_input() for now
"""
user_list = []

list = []

def make_list(user_input):
    for i in range (3):

        user_input = int(input("Please enter a number"))
        if user_input > 50:
            print('Error, wrong number')
        elif user_input < 0:
            print('None: negative number')
        else:
            raise ValueError('Wrong values/input')
        list.append(user_input)
        print("Value of list",list)
        return list

def get_input(list):
    print('return_value=' +str(list[1]))
    return ('return_value=' +(list[1]))

if __name__ == '__main__':
    make_list([3, 5, 6])
    get_input(list)
