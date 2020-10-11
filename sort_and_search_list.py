"""
Program: sort_and_search_list.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
Search and Sort List Assignment
You can make a new files test_sort_and_search_list.py and sort_and_search_list.py.
In the appropriate directories. For this assignment, you can hard-code a list you pass
to the sort_list() and search_list(). For extra credit, you and use the previous assignment get_list()
"""
list = [3,2,9,8,3,6,7,8]

def sort_list(list):
    list.sort()
    print("List sorted", list)
    return[list]

def search_list(index):
    print("The index is", list[5])
    index = list.index(7)
    return index

if __name__ == '__main__':
    sort_list(list)
    search_list(list)
