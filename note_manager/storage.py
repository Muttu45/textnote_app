
import json
from .note import Note


FILE_NAME = "notes.json"


def save_notes(notes_list):
    try:
        data = [note.save() for note in notes_list]

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    except (OSError, TypeError) as error:
        print(f"Error saving notes: {error}")


def load_notes():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        return [
            Note(
                item["title"],
                item["content"],
                item.get("tags", []),
                item.get("timestamp")
            )
            for item in data
        ]

    except FileNotFoundError:
        return []

    except (json.JSONDecodeError, KeyError, TypeError, OSError) as error:
        print(f"Error loading notes: {error}")
        return []
