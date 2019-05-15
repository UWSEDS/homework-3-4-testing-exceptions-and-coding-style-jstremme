# Homework 3-4: Coding style and Unit tests.

##### Grade: 9/14   

-2: dataframe.py - your test will pass even when the DF has no columns at all.  
-2: test_dataframe.py - test names should be more descriptive   
-1: test_dataframe.py - this might be outside the scope of this class since we are only starting to write tests, but I think this is an important point to make. In test_one_row(), you have self.assertFalse(data_frame.shape[0] < 1). Technically, this double negative works, but people usually (they should almost always!) prefer a single positive condition over a double negative condition.



-----

**Note: This homework has a total of 14 points.**

In this homework, you will create two python modules and put them in PEP8 style.

1. Function code (5 points). Last week you wrote python codes that read an online file and created a data frame that has at least 3 columns. Now: (a) create a python module ``dataframe.py`` that reads the data in homework 2;  and (b) ``dataframpe.py`` should generate an ValueError execption if the dataframe doesn't have the expected column names.

1. Test code (5 points). Create a python file ``test_dataframe.py`` that has unit tests for dataframe.py. Include at least 2 of the following tests:

   - You have the expected columns.
   - Values in the column are all of the expected type.
   - There are no nan values.
   - The dataframe has at least one row.
   
1. Coding style (4 points). Make all codes PEP8 compliant and provide the output from pylint to demonstrate that you have accomplished this.
