"""
pytests for main app
"""
from modules import Achievement
from datetime import datetime as dt
import pytest

def test_achievement_timestamp():
    """
    Basic test for
    :return: pass
    """
    rep1 = Achievement()
    assert isinstance(rep1.timestamp, dt)
