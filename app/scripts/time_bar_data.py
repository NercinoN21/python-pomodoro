"""
    Control of data on study time and
    break times entered by the user.

    @author Nercino Neto
"""


import re
from dataclasses import dataclass


@dataclass
class TimeData:
    study_time: int
    break_time: int
    long_break_time: int

    def date_in_seconds(self) -> list[int]:
        return [self.study_time * 60,
                self.break_time * 60,
                self.long_break_time * 60]


def checking_data(initial_data: dict) -> bool:
    """Checking user input"""

    regex_number = "^[0-9]+$"

    for value in initial_data.values():
        if not re.search(regex_number, value) or value[0] == "0":
            return False

    return True


def turning_data_into_int(initial_data: dict) -> list[int]:
    return [int(value) for value in initial_data.values()]
