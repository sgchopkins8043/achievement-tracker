"""
class & methods for achievement-tracker app
"""
from datetime import datetime as dt

class Achievement:
    """
    This is an achievement class
    """
    def __init__(self, category: str, team: str, achievement: str, context: str):
        self.timestamp = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        self.category = category
        self.team = team
        self.achievement = achievement
        self.context = context

    def flag(self):
        """
        dummy method
        :return:
        """


    def devops(self):
        """
        dummy method
        :return:
        """
