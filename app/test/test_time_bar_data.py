"""
    Testing "time_bar_data" functions and class

    @author Nercino Neto
"""


import unittest
import app.scripts.time_bar_data as tbd


class TestTimeBarData(unittest.TestCase):
    data = tbd.TimeData(50, 10, 15)

    sec_study, sec_break, sec_long_break = data.date_in_seconds()

    checking_true = tbd.checking_data({
        1: "100",
        2: "10",
        3: "1"
    })
    checking_false = tbd.checking_data({
        1: "N", 2: "2.2",
        3: "-1", 4: "02",
        5: "", 6: "5-1"
    })

    turning_data = tbd.turning_data_into_int({
        1: "100",
        2: "50",
        3: "25"
    })
    expected_outcome = [100, 50, 25]

    def test_time_data(self):
        self.assertEqual(self.data.study_time, 50)
        self.assertEqual(self.data.break_time, 10)
        self.assertEqual(self.data.long_break_time, 15)

    def test_date_in_seconds(self):
        self.assertEqual(self.sec_study, self.data.study_time * 60)
        self.assertEqual(self.sec_break, self.data.break_time * 60)
        self.assertEqual(self.sec_long_break, self.data.long_break_time * 60)

    def test_checking_data(self):
        self.assertTrue(self.checking_true)
        self.assertFalse(self.checking_false)

    def test_turning_data_into_int(self):
        self.assertEqual(self.turning_data, self.expected_outcome)


if __name__ == "__main__":
    unittest.main()
