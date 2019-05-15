'''This module runs tests on read_congress_terms() in dataframe.py'''

import unittest
from dataframe import read_congress_terms

class UnitTests(unittest.TestCase):
    '''This class contains the test functions to execute'''

    def test_rows_greater_than_one(self):
        '''Test that dataframe has at least one row'''

        data = read_congress_terms()
        self.assertTrue(data.shape[0] > 1)

    def test_expected_cols_present(self):
        '''Test that dataframe has the expected columns'''

        data = read_congress_terms()
        cols = ['firstname', 'lastname', 'termstart', 'age']
        self.assertTrue(set(cols) == set(data.columns))

if __name__ == '__main__':
    unittest.main()
    