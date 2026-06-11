# Bookmark Manager

## Description
This project is a simple command-line Bookmark Manager built with Python.

It allows users to store, organize, update, and delete website bookmarks with categories and timestamps.
Each bookmark behaves like a small structured record similar to a browser bookmark system.

The goal of this project is to practice building real-world CLI tools with structured data instead of simple task lists.

---

## What this project does
- Adds bookmarks with title, URL, and category
- Automatically normalizes URLs (adds https if needed)
- Stores bookmarks in a structured JSON file
- Displays all bookmarks in a table format
- Updates individual bookmark fields (partial update supported)
- Deletes bookmarks by selection
- Tracks creation and update timestamps

---

## Modules Used
- `pathlib` → file path handling
- `json` → storing bookmark data
- `uuid` → unique bookmark IDs
- `datetime` → timestamps
- `urllib.parse` → URL validation
- `pandas` → table display
- `string` → title cleaning

---

## Output Example
```
--- Bookmark Manager ---
1. Add Bookmark
2. View Bookmarks
3. Update Bookmark
4. Delete Bookmark
5. Exit
: 1

(Add 'q' to cancel)

Title: enjoy
Category: game
URL: https://sabirhusseinbalal.github.io/
Bookmark added successfully!
```
```
: 2

                                     id  title category                                      url           created_at
0  9dc41084-4646-4aae-acd2-881b392bf906  enjoy     game  https://sabirhusseinbalal.github.io/  2026-06-06 16:01:44
```

---

## Features
- Bookmark creation with validation
- URL normalization
- Category-based organization
- Structured JSON storage
- Partial update system
- Timestamp tracking
- Table-based CLI display

---

## Project Structure
```
08_bookmark_manager/
├── main.py
├── data.json
└── README.md
```

---

## Notes
- This project focuses on building real-world CLI tool behavior.
- Data is stored locally in JSON format.
- Update system supports partial field modification.
- Index-based selection is used for simplicity in CLI.
- This project introduces structured data thinking (not just task lists).
