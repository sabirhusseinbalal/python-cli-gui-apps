# Task Time Tracker

## Description
This project is a simple command-line Task Time Tracker built with Python.

It allows users to start a task, track elapsed time, stop the task, and save completed work sessions.

The project was built to practice time measurement, state management, application workflow design, and working with task sessions in a CLI application.

---

## What this project does
- Starts a task timer
- Tracks elapsed time while a task is running
- Stops active tasks
- Saves completed work sessions
- Displays saved session history
- Prevents invalid actions during tracking
---

## Modules Used
- `time` → measuring elapsed time
- `datetime` → storing session timestamps
- `pandas` → displaying session history in table format

---

## Output Example
```
--- Task Time Tracker ---
1. Start Task
2. Track Time
3. Stop Task
4. Save Session
5. Show History
6. Exit
: 1

Enter Task Title: Python

Tracking started for 'Python'.
```
```
Task: Python
Elapsed Time: 12.48 seconds
```
```
Task: Python
Final Time: 12.48 seconds

Now choose option 4 to save.
...
```
```
     task  duration_seconds           started_at             ended_at
0  Python             12.48  2026-06-06 12:23:59  2026-06-06 12:24:12
```

---

## Features
- Task timer start/stop system
- Real-time elapsed time tracking
- Session duration calculation
- Session history storage (runtime)
- Table view using Pandas
- Input validation
- Beginner-friendly CLI interface

---

## Project Structure
```
06_task_time_tracker/
├── main.py
└── README.md
```

---

## Notes
- Only one task can run at a time.
- A task must be stopped before it can be saved.
- Unsaved sessions are discarded when the program closes.
- Session history exists only while the program is running.
- Time is measured using Python's time.time() function.
- Built for learning time tracking, state management, and CLI application workflow design.
