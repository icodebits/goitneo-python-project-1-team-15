import unittest

from helpers.cli_parser import parse_input

class Test_CLI_Parser(unittest.TestCase):
    def test_parse_input_with_args(self):
        user_input = "command arg1 arg2 arg3"
        cmd, *args = parse_input(user_input)
        self.assertEqual(cmd, "command")
        self.assertEqual(args, ["arg1", "arg2", "arg3"])

    def test_parse_input_without_args(self):
        user_input = "command"
        cmd, *args = parse_input(user_input)
        self.assertEqual(cmd, "command")
        self.assertEqual(args, [])

    def test_parse_input_lowercase_command(self):
        user_input = "ComManD arg1 arg2"
        cmd, *args = parse_input(user_input)
        self.assertEqual(cmd, "command")
        self.assertEqual(args, ["arg1", "arg2"])

    def test_parse_input_with_spaces(self):
        user_input = "   command    arg1   arg2   "
        cmd, *args = parse_input(user_input)
        self.assertEqual(cmd, "command")
        self.assertEqual(args, ["arg1", "arg2"])

if __name__ == '__main__':
    unittest.main()
