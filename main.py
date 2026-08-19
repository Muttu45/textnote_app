
from note_manager import Note, save_notes, load_notes


def show_menu():
    print("\n===== NOTE MANAGER =====")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")


def add_note(notes):
    title = input("Enter title: ").strip()
    content = input("Enter content: ").strip()

    tags_input = input("Enter tags (comma-separated): ").strip()
    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

    note = Note(title, content, tags)
    notes.append(note)

    save_notes(notes)
    print("Note added successfully!")


def view_notes(notes):
    if not notes:
        print("No notes available.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"\nNote #{index}")
        note.display()


def search_notes(notes):
    term = input("Enter search keyword: ").strip()

    found = False

    for index, note in enumerate(notes, start=1):
        if note.matches_search(term):
            print(f"\nNote #{index}")
            note.display()
            found = True

    if not found:
        print("No matching notes found.")


def delete_note(notes):
    if not notes:
        print("No notes available.")
        return

    view_notes(notes)

    try:
        index = int(input("Enter note number to delete: "))

        if 1 <= index <= len(notes):
            deleted_note = notes.pop(index - 1)
            save_notes(notes)
            print(f"Deleted note: {deleted_note.title}")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    notes = load_notes()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            search_notes(notes)

        elif choice == "4":
            delete_note(notes)

        elif choice == "5":
            save_notes(notes)
            print("Notes saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
