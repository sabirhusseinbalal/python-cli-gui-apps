from pathlib import Path
import string

BASE_DIR = Path(__file__).resolve().parent
NOTES_DIR = BASE_DIR / "notes"
NOTES_DIR.mkdir(exist_ok=True)

# ClEAN TITLE
def clean_title(title):

    translator = str.maketrans('', '', string.punctuation)

    return title.lower().translate(translator).strip()

# MENU
def menu():
    while True:
        try:
            choice = int(input(
                "\n1. Create Note\n"
                "2. View Notes List\n"
                "3. Read Note\n"
                "4. Delete Note\n"
                "5. Search Note\n"
                "6. Exit\n: "
            ).strip())
            print()

            if choice in [1, 2, 3, 4, 5, 6]:
                return choice

        except ValueError:
            pass

        print("Invalid Choice!")

# GET NOTES
def get_notes():
    return [f for f in NOTES_DIR.glob("*.md")]

# CREATE_NOTE
def create_note():

    while True:
        title = input("Enter note title (or 'q'): ").lower().strip()

        if title == "q":
            return
        
        title = clean_title(title)

        if not title:
            print("Invalid title or empty title!")
            continue

        content = input("Enter content: ")

        if not content:
            print("Content cannot be empty!")
            continue

        output_file = NOTES_DIR / f"{title}.md"
        counter = 1

        while output_file.exists():
            output_file = NOTES_DIR / f"{title}_{counter}.md"
            counter += 1
        
        with output_file.open("w", encoding="utf-8") as f:
            f.write(content)

        clean_name = output_file.name

        print(f"{clean_name} - Note created successfully!")
        return


# VIEW NOTES
def view_notes():

    notes = get_notes()

    if len(notes) > 0:

        for i, note in enumerate(notes, start=1):
            print(f"Note {i}: {note.name}")
    else:
        print("No valid notes found.")


# READ_NOTE
def read_note():

    notes = get_notes()

    if len(notes) > 0:

        for note in NOTES_DIR.rglob("*"):
            if note.is_file():
                print(f"Note : {note.stem}")
        
        name = input("\nEnter exists name of note: ").lower().strip()

        file_path = NOTES_DIR / f"{name}.md"

        if file_path.exists():
            with file_path.open("r", encoding="utf-8") as f:
                print("\n" + "-" * 40)
                print(f.read())
                print("-" * 40)
            
        else:
            print("No note found.")
    else:
        print("No valid notes found.")

# DELETE_NOTE
def delete_note():

    notes = get_notes()

    if len(notes) > 0:

        for note in NOTES_DIR.rglob("*"):
            if note.is_file():
                print(f"Note : {note.stem}")
        
        name = input("\nEnter exists name of note: ").lower().strip()

        file_path = NOTES_DIR / f"{name}.md"

        if file_path.exists():
            file_path.unlink()
            print("Note Deleted Successfuly!")
        else:
            print("No note found.")
    else:
        print("No valid notes found.")

# SEARCH_NOTE
def search_note():

    names = []

    for f in NOTES_DIR.rglob("*"):
        if f.is_file():
            names.append(f.stem)
    

    if len(names) > 0:

        input_name = input("\nEnter note name: ").lower().strip()

        matches_lc = [name for name in names if input_name in name]
        if not matches_lc:
            print("No match!")
        else:
            print("List comprehension:", matches_lc)

    else:
        print("No valid notes found.")


# MAIN
def main():

    print("Manage Notes")

    while True:

        try:


            choice = menu()

            if choice == 1:
                create_note()

            elif choice == 2:
                view_notes()

            elif choice == 3:
                read_note()

            elif choice == 4:
                delete_note()
            
            elif choice == 5:
                search_note()

            else:
                print("Exiting...")
                break

        except Exception as e:
            print(f"Error: {e}")


main()