"""
pytests for main app
"""
from modules import Achievement


def test_achievement_timestamp():
    """
    Basic test for
    :return: pass
    """
    rep1 = Achievement('category', 'team', 'achievement', 'context')
    assert isinstance(rep1.timestamp, str)
