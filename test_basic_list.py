#Below assumes we are using unit tests

#Generally put your doc string at the Top.
#When you have modified and filled out the below doc string
#delete this line and the 2 lines above it
"""
Program: test_basic_list.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
Write a python file basic_list.py and declare two functions make_list()
with pass and get_input() with pass (function not written keyword).
Function make_list() will eventually return a list of user input while get_input()
will get one input and return it
"""
import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as basic_list


class MyTestCase(unittest.TestCase):
 def test_make_list(self):
   with patch('fun_with_collections.basic_list.get_input', return_value='9'):
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(input), [8, 6, 9])


if __name__ == '__main__':
    unittest.main()
