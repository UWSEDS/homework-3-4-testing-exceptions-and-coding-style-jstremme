'''This module contains functions for reading and manipulating a dataframe'''

import pandas as pd

def read_congress_terms():
    '''Read congress-terms.csv from fivethirtyeight github.
       The file congress-terms.csv has an entry for every
       member of congress who served at any point during
       a particular congress between January 1947 and Februrary 2014'''

    url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv'
    cols = ['firstname', 'lastname', 'termstart', 'age']
    data = pd.read_csv(url)
    for col in cols:
        if not col in data.columns:
            raise ValueError("DataFrame should have a column named '{}'".format(col))
    return data[cols]
    