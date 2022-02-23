"""
achievement app
"""
from modules import Achievement
import os
import pandas as pd


a = Achievement()

print(a.timestamp)

def open_dataframe():
    try:
        datafile = './data/data.csv'
        df = pd.read_csv(datafile)
        return df

    except IOError:
        print("problem")

open_dataframe()
