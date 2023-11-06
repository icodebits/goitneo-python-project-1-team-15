import unittest

from base.notes import Note, Notes

class Test_Note(unittest.TestCase):
    def test_note_creation(self):
        text = "Test note"
        tags = ["tag1", "tag2"]
        note = Note(text, tags)
        self.assertEqual(note.text, text)
        self.assertEqual(note.tags, tags)
    
    def test_note_creation_default_tags(self):
        text = "Test note"
        note = Note(text)
        self.assertEqual(note.text, text)
        self.assertEqual(note.tags, [])

    def test_note_string_representation(self):
        text = "Test note"
        tags = ["tag1", "tag2"]
        note = Note(text, tags)
        expected_str = f"{text} - Tags: {', '.join(tags)}"
        self.assertEqual(str(note), expected_str)

class Test_Notes(unittest.TestCase):
    def setUp(self):
        self.notes = Notes()
        self.notes.add_note("Buy milk", ["shop"])
        self.notes.add_note("Plan a trip")
        self.notes.add_note("Call the doctor", ["health"])
        self.notes.add_note("Plan a visit to parents", ["family", "parents"])

    def test_add_note(self):
        initial_count = len(self.notes.notes)
        result = self.notes.add_note("New note")
        self.assertEqual(result, "Note added")
        self.assertEqual(len(self.notes.notes), initial_count + 1)

    def test_search_notes(self):
        keyword = "plan"
        search_results = self.notes.search_notes(keyword)
        self.assertEqual(len(search_results), 2)
        for note in search_results:
            self.assertTrue(keyword in note.text.lower())

    def test_edit_note(self):
        index = 2
        new_text = "Plan a meeting with a friend"
        result = self.notes.edit_note(index, new_text)
        self.assertEqual(result, f"Note {index} updated")
        self.assertEqual(self.notes.notes[index - 1].text, new_text)

    def test_add_tags(self):
        index = 2
        tags = ["meeting"]
        result = self.notes.add_tags(index, tags)
        self.assertEqual(result, "Tags added")
        self.assertEqual(self.notes.notes[index - 1].tags, tags)

    def test_search_notes_by_tag(self):
        tag = "family"
        search_results = self.notes.search_notes_by_tag(tag)
        self.assertEqual(len(search_results), 1)
        for note in search_results:
            self.assertTrue(tag in [t.lower() for t in note.tags])

if __name__ == '__main__':
    unittest.main()
