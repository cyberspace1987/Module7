"""
Program: basic_list.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
In Module7, copy basic_list.py and name it basic_list_exception.py.
Create test_basic_list_exception.py in the test_collections directory
and include the function that tests the list from test_basic_list.py.
Leave the function get_input() for now
"""
import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as basic_list_exception


class MyTestCase(unittest.TestCase):
 def test_make_list(self):
   with patch('fun_with_collections.basic_list_exception.get_input', return_value='9'):
    def test_make_list(self, input):
        self.assertEqual(basic_list_exception.make_list(input), [6, 75, -9])


if __name__ == '__main__':
    unittest.main()
