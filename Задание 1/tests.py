import unittest
from md_converter_but_better import *

class TestConverter(unittest.TestCase):

    def test_get_titles(self) -> None:
        data = '# title Test Title\n# description Desc\n#Desc'
        title, lower_cased_title = get_titles(data)
        self.assertEqual(title, 'Test Title')
        self.assertEqual(lower_cased_title, 'test-title')

    def test_get_titles_empty(self) -> None:
        data = ''
        title, lower_cased_title = get_titles(data)
        self.assertEqual(title, '')
        self.assertEqual(lower_cased_title, '')

    def test_get_desc_code(self) -> None:
        data = '# title Test Title\n# description Desc\n#Desc\n#---end---\nprint("Hello World!")'
        desc, code = get_desc_code(data)
        self.assertEqual(desc, 'Desc\nDesc')
        self.assertEqual(code, 'print("Hello World!")')

    def test_get_desc_code_empty(self) -> None:
        data = ''
        desc, code = get_desc_code(data)
        self.assertEqual(desc, '')
        self.assertEqual(code, '')

if __name__ == "__main__":
    unittest.main()