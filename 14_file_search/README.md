# File Search

## Description
This project is a simple desktop file search application built using Python and PySide6.

It allows users to search files inside a selected folder using different search methods such as file name, extension, file size, or text inside files.

The main goal of this project is to understand how GUI applications interact with the file system and perform recursive file searching.

---

## What this project does
- Browse and select a folder
- Search files by file name
- Search files by extension
- Search files by maximum size (KB)
- Search text inside files
- Display matching files
- Show total number of matched files
- Handle invalid folders and invalid input safely

---

## How it works (simple logic)
1. User selects a folder (or uses the default input folder)
2. User chooses a search mode:
   - File Name
   - Extension
   - Maximum Size
   - File Content
2. User enters a search value.
3. The application recursively scans every file inside the selected folder.
4. Matching files are displayed in the results list along with their file size.

---

## Modules Used
- `sys` → run application
- `pathlib` → file path handling
- `PySide6` → GUI (buttons, inputs, layout, list)
- `QFileDialog` → browse folders

---

## GUI Preview
![GUI Preview](https://github.com/sabirhusseinbalal/python-cli-gui-apps/blob/main/14_file_search/image.PNG)

---

## Features
- Desktop GUI built with PySide6
- Folder browser
- Recursive file searching
- Four different search modes
- Search result list
- Total files found counter
- Beginner-friendly structure

---

## Project Structure
```
14_file_search/
├── input/
├── image.PNG
├── main.py
├── README.md
```

---

## Notes
- This project is designed for learning file system operations with a desktop GUI.
- Avoid searching very large directories such as the entire C:\ or D:\ drive because scanning thousands of files can take a long time.
- It is recommended to test the application using smaller folders or project directories.
- This project can be upgraded with:
    - open selected file
    - double-click to open
    - search progress bar
    - file type icons
    - sorting and filtering results

