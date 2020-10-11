"""
Program: test_sort_and_search_list.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
Search and Sort List Assignment
You can make a new files test_sort_and_search_list.py and sort_and_search_list.py.
In the appropriate directories. For this assignment, you can hard-code a list you pass
to the sort_list() and search_list(). For extra credit, you and use the previous assignment get_list()
"""
import unittest
import fun_with_collections.sort_and_search_list as basic_list_exception


class MyTestCase(unittest.TestCase):
    def test_make_list(self):
        self.assertTrue(basic_list_exception.sort_list([5, 3, 6, 8,9,10, 4]))
        basic_list_exception.search_list([3])


if __name__ == '__main__':
    unittest.main()
