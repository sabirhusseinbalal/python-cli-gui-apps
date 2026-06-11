# Account Vault Simulator

## Description
This project is a simple command-line Account Vault Simulator built with Python.

It allows users to store multiple online account details like platform, email, username, and password. Each account is protected using a unique Vault Code, which is used to access or delete the account later.

---

## What this project does
- Adds new account details (platform, email, username, password)
- Generates a unique vault code for each account
- Views all saved accounts in a clean list format
- Opens full account details using vault code
- Deletes accounts using vault code
- Stores data permanently using JSON file

---

## Modules Used
- `pathlib` → file path handling
- `json` → storing and loading data
- `uuid` → unique account IDs
- `random` + `string` → vault code generation
- `datetime` → timestamps

---

## Output Example
```
--- Account Vault Simulator ---
1. Add Account
2. View Accounts
3. Open Account
4. Update Account
5. Delete Account
6. Exit
: 1

(Add 'q' to cancel)

Platform: Facebook
Email: Iamloser@gmail.com
Username: sabirhusseinbalal
Password: 09idiot#3

Account created!
Vault Code: 4c4ay
```
```
: 2

--- Accounts ---
0. [4c4ay] facebook | sabirhusseinbalal
```
```
: 3
Enter Vault Code: 4c4ay

--- Account Details ---
Platform: facebook
Email   : Iamloser@gmail.com
Username: sabirhusseinbalal
Password: 09idiot#3
```

---

## Features
- Vault Code based access system
- Simple authentication check for updates
- Secure-style CLI structure (learning purpose only)
- JSON based permanent storage
- Real-world tool thinking approach

---

## Project Structure
```
account_vault_simulator/
├── vault.json
├── main.py
└── README.md
```

---

## Notes
- This is NOT a real password manager
- No encryption or security system is implemented
- Built only for learning CLI structure and data handling
- Vault Code acts as a simple lookup key system
