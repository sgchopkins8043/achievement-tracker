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

    def category(self):
        """
        This method takes an achievement object and returns the category attribute of the object
        :return: Category
        """

    def team(self):
        """
        This method takes an achievement object and returns the team attribute of the object
        :return: Team
        """
