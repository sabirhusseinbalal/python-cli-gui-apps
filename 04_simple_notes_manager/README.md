# Simple Notes Manager

## Description
This project is a simple command-line Notes Manager built with Python.

It allows users to create, read, search, and delete Markdown notes stored as local files.

The project was built to practice file handling, folder management, searching data, working with Markdown files, and organizing information through a CLI application.

---

## What this project does
- Creates new notes
- Stores notes as .md files
- Displays all available notes
- Reads note contents
- Searches notes by name
- Deletes notes when no longer needed

---

## Modules Used
- `pathlib` → file path handling
- `string` → cleaning note titles

---

## Output Example
```
Manage Notes

1. Create Note
2. View Notes List
3. Read Note
4. Delete Note
5. Search Note
6. Exit
: 1

Enter note title (or 'q'): Python
Enter content: 100 days of coding
python.md - Note created successfully!
```
```
: 5


Enter note name: py
List comprehension: ['python']
```

---

## Features
- Note creation
- Automatic filename cleaning
- Duplicate filename handling
- Note reading
- Note deletion
- Note searching
- Local file storage
- Beginner-friendly CLI interface

---

## Project Structure
```
04_simple_notes_manager/
├── notes/ 
│    ├── css.md 
│    ├── python.md 
│    └── ...
├── main.py
└── README.md
```

---

## Notes
- Notes are stored locally as (.md) files.
- Invalid punctuation is removed from note titles.
- Duplicate note names automatically receive a number suffix.
- Search works using partial name matching.
- This project focuses on file management rather than data persistence with JSON.
- Built for learning Python file handling, searching, and CLI application design.
