# GUI Todo App (SQLite + PySide6)

## Description
This project is a simple desktop Todo application built using Python with PySide6 and SQLite.

It allows users to manage daily tasks through a graphical interface instead of the command line.

Users can add tasks, view them in a list, mark them as completed, and delete them.  
All data is stored permanently using SQLite, so tasks are saved even after closing the application.

This project was built step-by-step to understand how real-world desktop applications work using GUI + database integration.

---

## What this project does
- Adds new tasks using a GUI input box
- Displays all tasks in a list widget
- Marks selected tasks as completed
- Deletes selected tasks
- Stores all data permanently using SQLite
- Automatically updates UI after every action

---

## Modules Used
- `sys` → application execution
- `sqlite3` → database handling
- `pathlib` → file path handling
- `PySide6.QtWidgets` → GUI components (buttons, input, list, layout)
- `datetime` → storing creation time (optional future upgrade)

---

## GUI Preview
![GUI Preview](image.png)

---

## Features
- Clean desktop GUI interface
- SQLite-based persistent storage
- Real-time UI updates
- Select + action-based task system
- Beginner-friendly PySide6 structure

---

## Project Structure
```
11_gui_todo_sqlite_app/
├── image.PNG
├── main.py
├── README.md
└── todo.db
```

---

## Notes
- This is the first GUI-based upgrade of the CLI Todo App
- Focus is on understanding how GUI connects with database logic
- PySide6 is used instead of Tkinter for modern desktop UI structure

