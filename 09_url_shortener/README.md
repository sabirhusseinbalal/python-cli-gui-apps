# URL Shortener

## Description
This project is a simple command-line URL Shortener built with Python.

It allows users to add long URLs and convert them into short unique codes. These codes can later be used to quickly open or delete saved links.

The project was built to practice real-world tool thinking, including mapping keys to values, data persistence using JSON, and working with the web browser module in Python.

---

## What this project does
- Adds long URLs to the system
- Generates a unique short code for each URL
- Opens URLs using the short code
- Deletes saved links using the code
- Displays all stored links in a clean list
- Stores data permanently using JSON file

---

## Modules Used
- `pathlib` → file path handling
- `json` → storing and loading data
- `uuid` → unique bookmark IDs
- `webbrowser` → opening links in browser
- `datetime` → timestamps
- `urllib.parse` → URL validation
- `random` + `string` → short code generation

---

## Output Example
```
Welcome to CLI URL Shortener (Real Tool)

--- URL Shortener ---
1. Add URL
2. View Links
3. Open Link
4. Delete Link
5. Exit
: 1
URL: https://sabirhusseinbalal.github.io

Short URL created!
Code: e5bs3
Use this code to open the link.
```
```
--- Saved Links ---
0. [e5bs3] → https://sabirhusseinbalal.github.io
```
```
Enter code: e5bs3
Opening: https://sabirhusseinbalal.github.io
```

---

## Features
- Real URL shortener logic (code → URL mapping)
- Automatic unique code generation
- Safe URL validation
- Open links directly from terminal
- Delete links using short code
- Persistent storage using JSON
- Beginner-friendly CLI interface

---

## Project Structure
```
09_url_shortener/
├── links.json
├── main.py
└── README.md
```

---

## Notes
- This is a local CLI-based URL shortener (not a web server)
- Codes are randomly generated and unique
- Data is stored permanently in JSON file
- URLs are validated before saving
