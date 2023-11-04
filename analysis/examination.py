import re
import json
import os

def load_commands(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            commands = json.load(file)
        return commands
    else:
        print(f"File '{file_path}' does not exist in the specified directory.")
        return {}

def analytics():
    user_choice = input("Choose 'contact' or 'notes': ").lower()
    if user_choice not in ['contact', 'notes']:
        print("Invalid choice. Please choose 'contact' or 'notes'.")
        return

    if user_choice == 'contact':
        file_path = os.path.join('analysis', 'resources', 'contact_commands.json')
    else:
        file_path = os.path.join('analysis', 'resources', 'notes_commands.json')

    keywords = load_commands(file_path)

    user_input = input("Enter a sentence (or 'back' to return to the selection menu): ")

    if user_input.lower() == 'back':
        return

    matches = {}
    max_matches = 0

    for keyword, template in keywords.items():
        keyword_parts = keyword.split()
        keyword_matches = 0

        for keyword_part in keyword_parts:
            if re.search(r'\b' + re.escape(keyword_part.lower()) + r'\b', user_input.lower()):
                keyword_matches += 1

        if keyword_matches > 0:
            matches[keyword] = keyword_matches
            max_matches = max(max_matches, keyword_matches)

    if matches:
        print("Possible commands with the maximum number of matches:")
        for keyword, keyword_matches in matches.items():
            if keyword_matches == max_matches:
                print(keywords[keyword])
        print("Do you see the command you wanted to use?\n"
              "If not, please copy your text and the desired command, and describe what you wanted or the command.\n"
              "We will be waiting for your response via email at helpapplicationmc3@gmail.com.")
    else:
        print("I can't find this command\n"
              "Please copy your text and the desired command, and describe what you wanted or the command.\n"
              "We will be waiting for your response via email at helpapplicationmc3@gmail.")

if __name__ == "__main__":
    analytics()
