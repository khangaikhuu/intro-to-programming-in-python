import unittest
from MyName import get_formatted_name
class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','', 'joplin')
        self.assertNotEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'amadeus','mozart')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()