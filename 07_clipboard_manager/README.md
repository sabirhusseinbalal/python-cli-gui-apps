# Clipboard Manager

## Description
This project is a simple command-line Clipboard Manager built with Python.

It allows users to copy text into the system clipboard, view clipboard content, paste it, and clear it when needed.

The project was built to understand how Python can interact with the operating system using external libraries and manage real clipboard data instead of storing values in variables or files.

---

## What this project does
- Copies text to system clipboard
- Displays current clipboard content
- Pastes clipboard content (simulated in CLI)
- Clears clipboard data
- Works with real system clipboard using `pyperclip`
---

## Modules Used
- `pyperclip` → system clipboard interaction

---

## Output Example
```
--- Clipboard Manager ---
1. Copy Text
2. Paste Clipboard
3. Show Clipboard
4. Clear Clipboard
5. Exit
: 1
Enter text to copy: Hello World!
Text copied to clipboard!
```
```
Pasted from clipboard:
Hello World!
```
```
--- Clipboard Content ---
Hello World!
```
```
Clipboard cleared!
```

---

## Features
- Real system clipboard integration
- Copy text from CLI
- Paste clipboard content
- View current clipboard state
- Clear clipboard instantly
- Simple and beginner-friendly CLI tool

---

## Project Structure
```
07_clipboard_manager/
├── main.py
└── README.md
```

---

## Notes
- This project interacts with the real system clipboard, not a simulated variable.
- Clipboard data is shared across all applications (browser, VS Code, etc.).
- Requires pyperclip library to work.
- This project introduces OS-level automation concepts.
- Built for learning real-world utility tool development in Python.
