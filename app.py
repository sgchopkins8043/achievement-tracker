"""
achievement app
"""
from modules import Achievement
import os
import pandas as pd



def open_dataframe():
    print("Checking for presence of data file......")
    try:
        datafile = './data/data.csv'
        df = pd.read_csv(datafile)
        print("File found.... loading into dataframe")
        return df

    except IOError:
        if input("File not found: Create new file? (Y/N)").lower() == 'y':
            initial = [Achievement('category field', 'team involved',
                                   'description of achievement', 'context of the report')]
            df = pd.DataFrame([vars(t) for t in initial])
            df.to_csv('./data/data.csv', index=False)

open_dataframe()
