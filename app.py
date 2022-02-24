"""
achievement app
"""
from modules import Achievement
import pandas as pd
import os as __os
import platform as __platform
from datetime import datetime as dt
from datetime import timedelta as td

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


def clear_screen():
    """
    Function to do a clear screen in Linux or Windows
    :rtype: None
    :return: None it clears the screen
    """
    if __platform.system() == "Windows":
        __os.system("cls")

    elif __platform.system() == "Linux":
        __os.system("clear")

    else:
        print("Your OS doesn't seem to be supported!")


def print_ten(df):
    pd.options.display.width = 0
    print(df.tail(10))

def print_last_14_days(df):
    pd.options.display.width = 0
    print(df[df['timestamp'] > (dt.now() - td(days=14)).strftime('%Y-%m-%d %H:%M:%S')])

def write_achievement(df):
    df1 = df.copy()
    category = input("Enter category of achievement: ")
    team = input("Enter team: ")
    achievement = input("Enter achievement: ")
    context = input("Enter Context: ")
    new = Achievement(category, team, achievement, context)
    data = [[new.timestamp, new.category, new.team, new.achievement, new.context]]
    df2 = pd.DataFrame(data, columns=['timestamp', 'category', 'team', 'achievement', 'context'])
    df = pd.concat([df1, df2], axis=0)
    df.to_csv('./data/data.csv', index=False)
    print(df)

def menu(df):
    option = input("Enter one of the following options:\n1. List last 10 records...\n2. List previous 14 days...\n3. Choose Time Period..\n4. Write new achievement..\n9. Exit..").lower()
    try:
        int(option)
    except ValueError:
        option = "0"
    if int(option) == 1:
        print_ten(df)
    elif int(option) == 2:
        print_last_14_days(df)
    elif int(option) == 3:
        print("3")
    elif int(option) == 4:
        df = write_achievement(df)
        return df
    elif int(option) == 9:
        print("Closing app...")
    else:
        clear_screen()
        menu()

df = open_dataframe()
menu(df)
df = pd.read_csv('./data/data.csv')

