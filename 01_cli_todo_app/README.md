# CLI Todo App

## Description
This project is a simple command-line Todo application built using Python.

It allows users to manage daily tasks by adding, viewing, updating, and deleting them.

All tasks are stored in a JSON file, so data is saved even after closing the program.

This project was built step-by-step to understand how real-world task management systems work at a basic level.

---

## What this project does
- Adds new tasks with unique IDs
- Shows all tasks in a clean table format
- Marks tasks as completed
- Deletes tasks from the system
- Saves all data permanently using JSON

---

## Modules Used
- `pathlib` → file path handling
- `json` → saving and loading tasks
- `uuid` → generating unique task IDs
- `datetime` → storing task creation time
- `pandas` → displaying tasks in table format

---

## Output Example
```
Welcome to Simple CLI Todo App!

1. Add tasks
2. View tasks
3. Mark tasks done
4. Delete tasks
5. Exit
: 1
Enter Task name (or 'q'): Python ML 
Task added successfully!
```
```
: 2

        name                                    id                  created_at   status
0  Python ML  4e9a4a9c-f612-47aa-b20a-d871dba3abb0  2026-06-03 13:34:09.411497  pending
1         JS  c604d671-bebd-41de-b0a3-6c2fa8d769db  2026-06-03 13:34:15.427405  pending
```
```
: 4

        name                                    id                  created_at     status
0  Python ML  4e9a4a9c-f612-47aa-b20a-d871dba3abb0  2026-06-03 13:34:09.411497    pending
1         JS  c604d671-bebd-41de-b0a3-6c2fa8d769db  2026-06-03 13:34:15.427405  completed

Enter task number: 1
Task deleted successfully!
```

---

## Features
- Simple and clean CLI interface
- Persistent storage using JSON
- Unique task tracking using UUID
- Status tracking (pending / completed)
- Beginner-friendly structure
- Safe data updates and deletion

---

## Project Structure
```
01_cli_todo_app/
├── data.json
├── main.py
└── README.md
```

---

## Notes
- This is a beginner-level project for learning Python fundamentals.
- Focus was on understanding CRUD logic and file persistence.
- Pandas is used only for better task visualization in CLI.
- Future versions can include priority system, timestamps filtering, and GUI upgrade.
