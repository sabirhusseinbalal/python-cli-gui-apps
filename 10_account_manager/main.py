from pathlib import Path
from datetime import datetime
import json
import uuid
import random
import string

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "vault.json"


# LOAD
def load_data():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def generate_vault_code(data):
    chars = string.ascii_lowercase + string.digits

    while True:
        code = "".join(random.choice(chars) for _ in range(5))
        if not any(item["vault_code"] == code for item in data):
            return code


def find_by_code(data, code):
    for item in data:
        if item["vault_code"] == code:
            return item
    return None


# MENU
def menu():
    while True:
        try:
            choice = int(input(
                "\n--- Account Vault Simulator ---\n"
                "1. Add Account\n"
                "2. View Accounts\n"
                "3. Open Account\n"
                "4. Update Account\n"
                "5. Delete Account\n"
                "6. Exit\n: "
            ).strip())

            if choice in [1, 2, 3, 4, 5, 6]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# ADD ACCOUNT
def add_account(data):
    print("\n(Add 'q' to cancel)\n")

    platform = input("Platform: ").strip()
    if platform.lower() == "q":
        return

    email = input("Email: ").strip()
    if email.lower() == "q":
        return

    username = input("Username: ").strip()
    if username.lower() == "q":
        return

    password = input("Password: ").strip()
    if password.lower() == "q":
        return

    if not platform or not email or not username or not password:
        print("All fields required!")
        return

    vault_code = generate_vault_code(data)

    data.append({
        "id": str(uuid.uuid4()),
        "vault_code": vault_code,
        "platform": platform.lower(),
        "email": email,
        "username": username,
        "password": password,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_data(data)

    print("\nAccount created!")
    print(f"Vault Code: {vault_code}")


# VIEW ACCOUNTS
def view_accounts(data):
    if not data:
        print("No accounts found!")
        return

    print("\n--- Accounts ---")
    for i, item in enumerate(data):
        print(f"{i}. [{item['vault_code']}] {item['platform']} | {item['username']}")


# OPEN ACCOUNT
def open_account(data):
    if not data:
        print("No accounts found!")
        return

    code = input("Enter Vault Code: ").strip().lower()

    acc = find_by_code(data, code)

    if not acc:
        print("Account not found!")
        return

    print("\n--- Account Details ---")
    print(f"Platform: {acc['platform']}")
    print(f"Email   : {acc['email']}")
    print(f"Username: {acc['username']}")
    print(f"Password: {acc['password']}")


# UPDATE ACCOUNT
def update_account(data):
    if not data:
        print("No accounts found!")
        return

    view_accounts(data)

    code = input("\nVault Code: ").strip().lower()
    acc = find_by_code(data, code)

    if not acc:
        print("Invalid vault code!")
        return

    # SECURITY CHECK
    email = input("Confirm Email: ").strip()
    password = input("Confirm Password: ").strip()

    if email != acc["email"] or password != acc["password"]:
        print("Authentication failed!")
        return

    print("\nPress Enter to keep old value\n")

    new_platform = input(f"Platform ({acc['platform']}): ").strip()
    new_username = input(f"Username ({acc['username']}): ").strip()
    new_password = input(f"Password (hidden): ").strip()

    if new_platform:
        acc["platform"] = new_platform.lower()

    if new_username:
        acc["username"] = new_username

    if new_password:
        acc["password"] = new_password

    acc["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_data(data)

    print("Account updated successfully!")


# DELETE ACCOUNT
def delete_account(data):
    if not data:
        print("No accounts found!")
        return

    view_accounts(data)

    code = input("Vault Code to delete: ").strip().lower()

    for i, item in enumerate(data):
        if item["vault_code"] == code:
            confirm = input("Are you sure? (y/n): ").lower()
            if confirm == "y":
                removed = data.pop(i)
                save_data(data)
                print(f"Deleted: {removed['platform']}")
            return

    print("Account not found!")


# MAIN 
def main():
    print("Account Vault Simulator")

    data = load_data()

    while True:
        choice = menu()

        if choice == 1:
            add_account(data)

        elif choice == 2:
            view_accounts(data)

        elif choice == 3:
            open_account(data)

        elif choice == 4:
            update_account(data)

        elif choice == 5:
            delete_account(data)

        else:
            print("Exiting...")
            break


main()