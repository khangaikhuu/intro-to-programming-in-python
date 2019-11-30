import unittest
from survey import Anonymous
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class Anonymous"""
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = Anonymous(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
        # CI / CD
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = Anonymous(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == "__main__":
    unittest.main()