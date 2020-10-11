"""
Program: sort_and_search_arrary.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
You can make a new files test_sort_and_search_array.py
and sort_and_search_array.py.
In the appropriate directories.
For this assignment, you can hard-code a list you pass to the sort_array()
and search_array(). For extra credit, you and use the previous assignment get_list()
"""
import array as arr

#from sort_and_search_array import *
def sort_array(lst, item):
    a = arr.array('i',[1,2,3])
    print("This is my first array test: ", end =" ")
    for i in range (0,3):
        print(a[i], end = " ")
        print()
    b = arr.array('d', [2.5, 3.2, 3.3])
    print("The other array test: ", end = " ")
    for i in range (0, 3):
        print(b[i], end = " ")
    #honestly I didn't inlcude a return is because I'm still learning more about return statements

def search_array(lst, item):
    for i in lst:
        if item == i:
            return i
    return -1

if __name__ == '__main__':
    pass
