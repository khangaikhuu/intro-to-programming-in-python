# Lesson-08
# Unit Tests
def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

# Unit Tests and Test Cases
import unittest
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
if __name__ == '__main__':
    unittest.main()


def test_first_last_middle_name(self):
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

"""
Ex.8.1
City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country , such as Santiago, Chile . Store the function in a module called
city _functions.py.
Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.

Ex.8.2
Population: Modify your function so it requires a third parameter,
population . It should now return a single string of the form City, Country –
population xxx , such as Santiago, Chile – population 5000000 . Run test
_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run test
_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that veri-
fies you can call your function with the values 'santiago' , 'chile' , and
'population=5000000' . Run test_cities.py again, and make sure this new test
passes.
"""

# Testing a Class

# A Variety of Assert Methods
"""
Method                          Use
assertEqual(a, b)               Verify that a == b
assertNotEqual(a, b)            Verify that a != b
assertTrue(x)                   Verify that x is True
assertFalse(x)                  Verify that x is False
assertIn(item, list)            Verify that item is in list
assertNotIn(item, list)         Verify that item is not in list
"""
# LINUS TORVALDS -  Linux Kernel
# Alone -> 
# Git -> CI/CD
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    def show_question(self):
        """Show the survey question."""
        print(self.question)    
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()


# The setUp() Method
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
"""
Ex.8.3
Employee: Write a class called Employee . The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee . Write two test methods, test_give_default
_raise() and test_give_custom_raise() . Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.
"""


# Machine learning with Python
# 