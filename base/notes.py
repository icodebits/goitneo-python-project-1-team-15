class Note:
    def __init__(self, text, tags=None):
        self.text = text
        self.tags = tags if tags is not None else []
    
    def __str__(self) -> str:
        tags_ = ", ".join(self.tags) if self.tags else "No tags"
        return (f"{self.text} - Tags: {tags_}")

class Notes:
    def __init__(self):
        self.notes = []

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except IndexError:
                return "Invalid note index."
        return inner

    def add_note(self, text, tags=None):
        note = Note(text, tags)
        self.notes.append(note)

    def search_notes(self, keyword):
        keyword = keyword.lower()
        matching_notes = [note for note in self.notes if keyword in note.text.lower()]
        return matching_notes

    @input_error
    def edit_note(self, index, new_text, new_tags=None):
        note = self.notes[index-1]
        note.text = new_text
        note.tags = new_tags if new_tags is not None else []
        return f"Note {index} updated"

    @input_error
    def delete_note(self, index):
        del self.notes[index-1]
        return f"Note {index} deleted"

    def display_notes(self):
        for i, note in enumerate(self.notes):
            print(f"{i + 1}. {note}")

    def add_tags(self, index, tags):
        note = self.notes[index-1]
        note.tags = tags if tags is not None else []
        return f"Tags added"
    
    def search_notes_by_tag(self, tag):
        tag = tag.lower()
        matching_notes = [note for note in self.notes if tag in [t.lower() for t in note.tags]]
        return matching_notes

    def sort_notes_by_tag(self):
        sorted_notes = sorted(self.notes, key=lambda note: sorted(note.tags))
        return sorted_notes

if __name__ == "__main__":
    # Class usage example:
    my_notes = Notes()
    my_notes.add_note("Buy milk", ["shop"])
    my_notes.add_note("Plan a trip")
    my_notes.add_note("Call the doctor", ["health"])
    my_notes.add_note("Plan a visit to parents",["family", "parents"])

    print("\nAll notes:")
    my_notes.display_notes()

    add_tags_result = my_notes.add_tags(2, ["trip"])
    print(f"\n {add_tags_result}")

    print("\nAll notes:")
    my_notes.display_notes()

    sort_results = my_notes.sort_notes_by_tag()
    print(f"\nSorted notes by tags:")
    for note in sort_results:
        print(note)

    search_keyword = "plan"
    search_results = my_notes.search_notes(search_keyword)
    print(f"\nNotes that contain '{search_keyword}' keyword:")
    for note in search_results:
        print(note)

    edit_result = my_notes.edit_note(2, "Plan a meeting with a friend")
    print(f"\n {edit_result}")

    print("\nAll notes (after edit):")
    my_notes.display_notes()

    delete_result = my_notes.delete_note(1)
    print(f"\n {delete_result}")

    print("\nAll notes (after delete):")
    my_notes.display_notes()

    delete_result = my_notes.delete_note(2)
    print(f"\n {delete_result}")

    print("\nAll notes (after another delete):")
    my_notes.display_notes()

    search_tag = "family"
    search_tag_results = my_notes.search_notes_by_tag(search_tag)
    print(f"\nNotes that contain tag '{search_tag}':")
    for note in search_tag_results:
        print(note)
