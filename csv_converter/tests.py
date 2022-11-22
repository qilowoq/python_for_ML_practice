import unittest
from manual import ManualCSVConverter
from builtin import BuiltInCSVConverter


class TestConverter(unittest.TestCase):

    def test_convert_csv_to_json_only_header(self) -> None:
        c1 = ManualCSVConverter()
        c2 = BuiltInCSVConverter()
        data = ['id,name,birth,salary,department']
        self.assertEqual(c1.to_json(data), '[]')
        self.assertEqual(c2.to_json(data), '[]')

    def test_convert_csv_to_json(self) -> None:
        c1 = ManualCSVConverter()
        c2 = BuiltInCSVConverter()
        data = ['id,name,birth,salary,department\n', '3,Ivan,1960,130000,8']
        json_data = """[
    {
        "id": "3",
        "name": "Ivan",
        "birth": "1960",
        "salary": "130000",
        "department": "8"
    }
]"""
        self.assertEqual(c1.to_json(data), '[{"id": "3", "name": "Ivan", "birth": "1960", "salary": "130000", "department": "8"}]')
        self.assertEqual(c2.to_json(data), json_data)

    def test_convert_csv_to_json_with_skips(self) -> None:
        c1 = ManualCSVConverter()
        c2 = BuiltInCSVConverter()
        data = ['id,name,birth,salary,department\n', '3,Ivan,,130000,8']
        json_data = """[
    {
        "id": "3",
        "name": "Ivan",
        "birth": "",
        "salary": "130000",
        "department": "8"
    }
]"""
        self.assertEqual(c1.to_json(data), '[{"id": "3", "name": "Ivan", "birth": "", "salary": "130000", "department": "8"}]')
        self.assertEqual(c2.to_json(data), json_data)

        
if __name__ == "__main__":
    unittest.main()