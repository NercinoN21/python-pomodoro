'''
    Control of data on study time and 
    break times entered by the user.

    @author Nercino Neto
'''

# Native
import re
from dataclasses import dataclass


@dataclass
class TimerData:
    study_time: int
    break_time: int
    long_break_time: int