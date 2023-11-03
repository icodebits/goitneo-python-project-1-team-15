import unittest

from analysis.examination import analytics, load_commands

class Test_Analysis(unittest.TestCase):
    def test_valid_load_commands(self):
        commands = load_commands('analysis/resources/contact_commands.json')
        self.assertTrue(commands)
    
    def test_invalid_load_commands(self):
        commands = load_commands('analysis/resources/non_existent_file.json')
        self.assertEqual(commands, {})

    def test_valid_contact_analytics(self):
        user_input = "Please call John Smith."
        expected_output = "Call John Smith"
        with unittest.mock.patch('builtins.input', side_effect=['contact', user_input, 'back']):
            self.assertEqual(analytics(), expected_output)
    
    def test_valid_notes_analytics(self):
        user_input = "Remind me to buy milk."
        expected_output = "Remind me to buy milk"
        with unittest.mock.patch('builtins.input', side_effect=['notes', user_input, 'back']):
            self.assertEqual(analytics(), expected_output)

    def test_invalid_choice_analytics(self):
        user_input = "invalid_choice"
        expected_output = "Invalid choice. Please choose 'contact' or 'notes'."
        with unittest.mock.patch('builtins.input', side_effect=['invalid_choice', 'back']):
            self.assertEqual(analytics(), expected_output)
    
    def test_no_matches_analytics(self):
        user_input = "This is a random sentence."
        expected_output = "I can't find this command\nPlease copy your text and the desired command, and describe what you wanted or the command.\nWe will be waiting for your response via email at helpapplicationmc3@gmail.com."
        with unittest.mock.patch('builtins.input', side_effect=['contact', user_input, 'back']):
            self.assertEqual(analytics(), expected_output)

if __name__ == '__main__':
    unittest.main()
