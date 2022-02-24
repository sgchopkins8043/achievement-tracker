"""
pytests for main app
"""
from datetime import datetime as dt
from modules import Achievement


def test_achievement_timestamp():
    """
    Basic test for
    :return: pass
    """
    rep1 = Achievement()
    assert isinstance(rep1.timestamp, dt)
