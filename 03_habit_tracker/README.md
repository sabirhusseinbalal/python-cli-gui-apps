# Habit Tracker

## Description
This project is a simple command-line Habit Tracker built with Python.

It allows users to create habits, track how many times they have been completed, and store habit history in a JSON file.

The project was built to practice state management, JSON storage, data persistence, and working with collections of records in a CLI application.

---

## What this project does
- Creates new habits
- Tracks habit completion count
- Stores completion history
- Displays all habits in a table
- Deletes habits when no longer needed
- Saves data between program runs

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
1. Add Habit
2. View Habits
3. Mark Habit Done
4. Delete Habit
5. Exit
: 1

Enter Habit name (or 'q'): Drink Water

Habit added successfully!
```
```
           name  completed
0   Drink Water          1
1  Milk+Almonds          0
2    10 Push-up          0
```
```
Enter habit number: 0

Today's Habit counted!
```

---

## Features
- Habit creation
- Habit completion tracking
- Completion history storage
- JSON-based persistence
- Table view using Pandas
- Unique ID generation
- Beginner-friendly CLI interface

---

## Project Structure
```
03_habit_tracker/
├── data.json
├── main.py
└── README.md
```

---

## Notes
- This project stores data locally in a JSON file.
- Each habit receives a unique ID using UUID.
- Completion history is stored as timestamps.
- This project tracks total completions, not daily streaks.
- Streak calculations could be added in a future version.
- Built for learning Python CLI application design and state management.
