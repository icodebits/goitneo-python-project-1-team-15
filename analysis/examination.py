import re
import json
import os


class CommandAnalyzer:
    def __init__(self):
        self.commands = None

    def load_commands(self, context):
        if context == "contact":
            file_path = os.path.join("analysis", "resources", "contact_commands.json")
        elif context == "notes":
            file_path = os.path.join("analysis", "resources", "notes_commands.json")
        else:
            print("Invalid context for analysis. Use 'contact' or 'notes'.")
            return

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                self.commands = json.load(file)
        else:
            print(f"File '{file_path}' does not exist in the specified directory.")
            self.commands = {}

    def analyze(self, context):
        self.load_commands(context)

        user_input = input(
            "Enter a sentence (or 'back' to return to the selection menu): "
        )

        if user_input.lower() == "back":
            return

        matches = {}
        max_matches = 0

        for keyword, template in self.commands.items():
            keyword_parts = keyword.split()
            keyword_matches = 0

            for keyword_part in keyword_parts:
                if re.search(
                    r"\b" + re.escape(keyword_part.lower()) + r"\b", user_input.lower()
                ):
                    keyword_matches += 1

            if keyword_matches > 0:
                matches[keyword] = keyword_matches
                max_matches = max(max_matches, keyword_matches)

        if matches:
            print("Possible commands with the maximum number of matches:")
            for keyword, keyword_matches in matches.items():
                if keyword_matches == max_matches:
                    print(self.commands[keyword])
            print(
                "Do you see the command you wanted to use?\n"
                "If not, please copy your text and the desired command, and describe what you wanted or the command.\n"
                "We will be waiting for your response via email at helpapplicationmc3@gmail.com"
            )
        else:
            print(
                "I can't find this command\n"
                "Please copy your text and the desired command, and describe what you wanted or the command.\n"
                "We will be waiting for your response via email at helpapplicationmc3@gmail.com"
            )
