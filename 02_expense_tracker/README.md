# Expense Tracker

## Description
This project is a simple command-line expense tracker.

It allows users to record earnings and expenses, calculate the current balance, and manage transaction history.

This project helped me understand how financial records, CRUD operations, and balance calculations work in real applications.

---

## What this project does
- Records earning transactions
- Records expense transactions
- Calculates current balance
- Tracks total earnings
- Tracks total expenses
- Updates existing transactions
- Deletes transactions
- Displays transaction history in table format

---


## Modules Used
- `uuid` → generating unique task IDs
- `datetime` → storing task creation time
- `pandas` → displaying tasks in table format

---

## Output Example
**Add Earning:**
```
1. Earning
2. Expense
3. Check Balance
4. Update Transaction
5. Exit
: 1

Enter Text (or 'q'): Salary
Enter Amount: 1000

Earning transaction added successfully!
```
**Add Expense:**
```
: 2

Enter Text (or 'q'): Internet Bill
Enter Amount: 200

Expense transaction added successfully!
```
**Check Balance:**
```
: 3

Current balance is positive.

Balance : 800$
Earnings: 1000$
Expenses: 200$
```
**Transaction History:**
```
            text  amount                    datetime                                    id   status
0         Salary    1000  2026-06-03 19:58:44.254756  daa4b7a2-fceb-4188-8852-f1dea0fc8174  Earning
1  Internet Bill     200  2026-06-03 20:01:51.262764  46adeb07-0be2-4f69-8d4b-840d477f96cc  Expense
```
**Update Transaction:**
```
Enter transaction number: 0

1. Edit Transaction
2. Delete Transaction
: 1

Enter New Amount: 1200

Transaction updated successfully!
```
---

## Features
- Earnings tracking
- Expense tracking
- Balance calculation
- Transaction history
- Transaction editing
- Transaction deletion
- Unique transaction IDs
- Table-based transaction display
- Beginner-friendly CLI interface

---

## Project Structure
```
02_expense_tracker/
├── main.py
└── README.md
```

---

## Notes
- This is an educational finance tracking project.
- All data is stored in memory and resets when the program closes.
- Real expense tracking applications usually save data in databases or files.
- Unique IDs help identify transactions reliably.
- Financial applications must carefully update balances whenever transactions are edited or deleted.
- Built for learning Python functions, lists, dictionaries, CRUD operations, and CLI application design.
