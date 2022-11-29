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

    def date_in_seconds(self) -> list[int] :
        """Converts from minutes to seconds.

        Returns:
            list[int]: Returns the variables 
            in "self" multiplied by 60
        """
        
        return [self.study_time * 60,
                self.break_time * 60,
                self.long_break_time * 60]

def checking_data(initial_data: dict) -> bool:

    regex_number = "^[0-9]+$"
    for value in initial_data.values():
        if not re.search(regex_number, value) or value[0] == "0": 
             return False

    return True