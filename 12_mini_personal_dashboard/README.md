# Mini Personal Dashboard

## Description
This project is a mini personal dashboard built using Python and PySide6.

It acts as a central hub that connects multiple previous projects like Todo App, Bookmark Manager, URL Shortener, and Vault system.

Instead of opening each project manually, this dashboard provides a single place to view quick stats and launch them.

This project was built to understand how real-world “system dashboards” work at a basic level.

---

## What this project does
- Shows a clean dashboard UI using PySide6
- Displays current date and day
- Shows quick summary of multiple projects:
   - Todo tasks (pending / completed)
   - Number of saved bookmarks
   - Number of shortened URLs
   - Number of vault accounts
- Opens other projects directly with one click
- Reads data from existing JSON files

---

## Modules Used
- `sys` → application execution
- `json` → reading project data
- `pathlib` → file path handling
- `datetime` → date display
- `subprocess` → opening other Python apps
- `PySide6` → GUI framework

---

## GUI Preview
![GUI Preview](image.png)

---

## Features
- Central control panel for multiple Python apps
- Live summary from real project data
- Simple GUI navigation system
- Lightweight design (no database needed)
- Beginner-friendly PySide6 structure

---

## Project Structure
```
12_mini_personal_dashboard/
├── image.PNG
├── main.py
├── README.md
```

---

## Notes
- This is a “mini system integration project”
- No new database is created here
- It reuses data from previous projects
- This is a step toward real-world software architecture thinking

