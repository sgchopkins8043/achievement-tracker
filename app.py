"""
achievement app
"""
import os as __os
import platform as __platform
from datetime import datetime as dt
from datetime import timedelta as td
import pandas as pd
from modules import Achievement


def open_dataframe():
    """
    Function to open the dataframe if it exists, or create a new one if it does not
    :return: Dataframe
    """
    print("Checking for presence of data file......")
    try:
        datafile = './data/data.csv'
        dataframe = pd.read_csv(datafile)
        print("File found.... loading into dataframe")
        return dataframe

    except IOError:
        if input("File not found: Create new file? (Y/N)").lower() == 'y':
            initial = [Achievement('category field', 'team involved',
                                   'description of achievement', 'context of the report')]
            dataframe = pd.DataFrame([vars(t) for t in initial])
            dataframe.to_csv('./data/data.csv', index=False)
            return dataframe
    return dataframe


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


def print_ten(dataframe):
    """
    Function to print last 10 records from the dataframe
    :param dataframe:
    :return: Last 10 records from dataframe
    """
    pd.options.display.width = 0
    print(dataframe.tail(10))


def print_last_14_days(dataframe):
    """
    Function to print last 14 days worth of records
    :param dataframe:
    :return: Last 14 days of records from dataframe
    """
    pd.options.display.width = 0
    print(dataframe[dataframe['timestamp'] > (dt.now()
                - td(days=14)).strftime('%Y-%m-%d %H:%M:%S')])


def write_achievement(dataframe):
    """
    Function to write a new achievement to the dataframe
    :param dataframe:
    :return: updated dataframe
    """
    df_main1 = dataframe.copy()
    category = input("Enter category of achievement: ")
    team = input("Enter team: ")
    achievement = input("Enter achievement: ")
    context = input("Enter Context: ")
    new = Achievement(category, team, achievement, context)
    data = [[new.timestamp, new.category, new.team, new.achievement, new.context]]
    df_main2 = pd.DataFrame(data, columns=['timestamp',
                'category', 'team', 'achievement', 'context'])
    dataframe = pd.concat([df_main1, df_main2], axis=0)
    dataframe.to_csv('./data/data.csv', index=False)
    print(dataframe)


def menu(dataframe):
    """
    Function to display menu options and call other functions
    :param dataframe:
    :return: dataframe
    """
    option = input("Enter one of the following options:\n1. List last 10 records...\n2. "
                   + "List previous 14 days...\n4. "
                   + "Write new achievement..\n9. Exit..").lower()
    try:
        int(option)
    except ValueError:
        option = "0"
    if int(option) == 1:
        print_ten(dataframe)
        menu(dataframe)
    elif int(option) == 2:
        print_last_14_days(dataframe)
        menu(dataframe)
    elif int(option) == 4:
        write_achievement(dataframe)
    elif int(option) == 9:
        print("Closing app...")
    else:
        clear_screen()
        menu(dataframe)


df_main = open_dataframe()
menu(df_main)
