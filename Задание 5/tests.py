import unittest
from isdayoff import IsDayOff
from main import calc_salary
import json

# run server before running tests
class TestComplex(unittest.TestCase):
    def setUp(self) -> None:
        self.isdayoff = IsDayOff()

    def test_isdayoff(self):
        res = self.isdayoff.number_of_work_days_in_month(2022, 8)
        self.assertEqual(res, 23)

    def test_all(self):
        input_json = {
            "year": 2022, 
            "month": 10, 
            "salary": 120000
            }
        output_json = {
            "year": 2022,
            "month": 10, 
            "salary": 120000, 
            "hour_income": 714.29
            }
        result = calc_salary(input_json)
        self.assertEqual(json.loads(result), output_json)


if __name__ == "__main__":
    unittest.main()