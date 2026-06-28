# Desktop Reminder App

## Description
This project is a simple desktop reminder application built using Python, PySide6, and SQLite.

It allows users to create time-based reminders that trigger desktop notifications when the time is reached.

All reminders are stored in a local SQLite database, so data is saved even after closing the app.

This project was built to understand how real-time background checking + GUI + database systems work together.

---

## What this project does
- Adds reminders with title and time (in minutes)
- Stores reminders in SQLite database
- Continuously checks reminders every second
- Shows desktop notification when time is reached
- Marks reminders as completed automatically
- Deletes reminders manually
- Shows live stats (Waiting / Completed / Total)

---

## How it works (simple logic)
1. User enters:
   - Title (what to remind)
   - Minutes (after how long)

2. System calculates:
   - current time + minutes → target_time

3. Every second:
   - app checks database
   - if current time >= target_time
     → show notification
     → mark as Completed

---

## Modules Used
- `sys` → run application
- `sqlite3` → database storage
- `pathlib` → file path handling
- `datetime` → time calculations
- `plyer` → desktop notifications
- `PySide6` → GUI (buttons, inputs, layout, list)
- `QTimer` → runs background check every second

---

## GUI Preview
![GUI Preview](https://github.com/sabirhusseinbalal/python-cli-gui-apps/blob/main/13_desktop_reminder_app/image.PNG)

---

## Features
- Simple GUI reminder system
- Time-based notifications
- Auto background checker (every 1 second)
- Persistent storage using SQLite
- Live task statistics
- Delete functionality
- Clean and beginner-friendly structure

---

## Project Structure
```
13_desktop_reminder_app/
├── image.PNG
├── list.db
├── main.py
├── README.md
```

---

## Notes
- This is a beginner-friendly real-world automation project
- Focus is on understanding background processing + UI updates
- Can be upgraded to:
  - recurring reminders
  - snooze system
  - sound alerts
  - task history tracking

