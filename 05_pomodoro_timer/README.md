# Pomodoro Timer

## Description
This project is a simple command-line Pomodoro Timer system built with Python.

It helps users manage focused study/work sessions using timers for Pomodoro sessions, short breaks, long breaks, and custom timers.

The main goal of this project is to practice working with time-based programs, loops, program control flow, and handling interruptions like Ctrl + C in a clean way.

---

## What this project does
- Starts a 25-minute Pomodoro focus session
- Starts short and long break timers
- Allows custom countdown timers
- Shows live countdown in the terminal
- Lets user stop timer anytime using Ctrl + C
- Safely returns back to menu after stopping

---

## Modules Used
- `time` → handling countdown and delays
- `os` → clearing terminal screen

---

## Output Example
```
--- Pomodoro System ---
1. Pomodoro (25 min)
2. Short Break (5 min)
3. Long Break (15 min)
4. Custom Timer
5. Exit
: 1
```
**Pomodoro Session:**
```
Press Ctrl+C to stop and return to menu

Pomodoro Session
24:51


Timer stopped by user.
Press Enter to return to menu...
```
**Break Session:**
```
Press Ctrl+C to stop and return to menu

Short Break
05:00
04:49
...
```
**Custom Timer:**
```
: 4
Enter timer label: Milkshake 
Enter seconds: 60
```
```
Press Ctrl+C to stop and return to menu

Milkshake
00:01

Milkshake finished!
Press Enter to return to menu...
```
---

## Features
- Pomodoro focus timer (25 min)
- Short break timer (5 min)
- Long break timer (15 min)
- Custom timer input
- Real-time countdown display
- Ctrl + C interrupt handling
- Clean return to menu system
- Beginner-friendly CLI interface

---

## Project Structure
```
05_pomodoro_timer/
├── main.py
└── README.md
```

---

## Notes
- This project is not about storing data, but about controlling time and execution flow.
- Ctrl + C no longer crashes the program; it safely returns to the menu.
- The timer engine is reusable for all session types.
- This is the first step toward building real productivity tools like Pomodoro systems and task trackers.
