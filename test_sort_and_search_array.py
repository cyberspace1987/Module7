"""
Program: test_sort_and_search_array.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
You can make a new files test_sort_and_search_array.py
and sort_and_search_array.py.
In the appropriate directories.
For this assignment, you can hard-code a list you pass to the sort_array()
and search_array(). For extra credit, you and use the previous assignment get_list()
"""


import unittest
#if we are mocking user typed in input
import unittest.mock as mock
#import file to test
from fun_with_collections import sort_and_search_array as main_test

class MyTestCase(unittest.TestCase):

    #notice all tests must start with test_* for the name
    def test_basic(self):
        #commonly can use:
            #assertTrue(), assertEqual(), assertFalse(), assertRaises()
        #basic function call
        self.assertEqual(main_test.search_array('lst','item'), -1)
        #above equals none because hello world just prints; doens't return
    def test_basic(self):
        #commonly can use:
            #assertTrue(), assertEqual(), assertFalse(), assertRaises()
        #basic function call
        self.assertEqual(main_test.sort_array('lst','item'), None)
        #above equals none because hello world just prints; doens't return
    #another test; still test_* for the name
    #def test_call_with_value(self):
        #self.assertEqual(main_test.search_array(lst,item), main_test.search_array(lst,item))

    #def test_one_input_mock(self):
        #notice this line
        #with mock.patch('builtins.input', return_value="turtle"):
            #self.assertEqual("turtle", main_test.get_user_input_once())

    #def test_multiple_input_mock(self):
        #notice this line
        #with mock.patch('builtins.input', side_effect=["turtle", "penguin"]):
            #self.assertEqual("You input turtle and penguin.", main_test.get_user_input_twice())

if __name__ == '__main__':
    unittest.main()
