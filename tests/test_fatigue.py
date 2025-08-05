import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from character import Character
from settings import FATIGUE_WORK_RATE, FATIGUE_IDLE_RATE, FATIGUE_MAX, COLLAPSE_SLEEP_TICKS


def test_fatigue_accumulation_and_reset():
    char = Character("Bob", (0, 0), role="forgeron", gender="homme")
    char.update_fatigue(working=True)
    assert char.fatigue == FATIGUE_WORK_RATE
    char.update_fatigue(working=False)
    assert char.fatigue == FATIGUE_WORK_RATE + FATIGUE_IDLE_RATE
    char.update_fatigue(working=False, sleeping=True)
    assert char.fatigue == 0


def test_fatigue_forces_sleep():
    char = Character("Bob", (0, 0), role="forgeron", gender="homme")
    char.fatigue = FATIGUE_MAX - FATIGUE_WORK_RATE
    char.update_fatigue(working=True)
    assert char.sleep_timer == COLLAPSE_SLEEP_TICKS
