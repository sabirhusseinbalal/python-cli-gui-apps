from pathlib import Path
from datetime import datetime
import pandas as pd
import uuid
import json

BASE_DIR = Path(__file__).resolve().parent


# SAVE DATA
def save_data(json_file, data):
    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# LOAD DATA
def load_data(json_file):
    if json_file.exists():
        try:
            with json_file.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


# MENU
def menu():
    while True:
        try:
            choice = int(input(
                "\n1. Add tasks\n"
                "2. View tasks\n"
                "3. Mark tasks done\n"
                "4. Delete tasks\n"
                "5. Exit\n: "
            ).strip())

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
            pass

        print("Invalid Choice!")


# ADD TASK
def add_task(json_file, data):

    while True:
        name = input("Enter Task name (or 'q'): ").strip()

        if name.lower() == "q":
            return

        if not name:
            print("Task name cannot be empty!")
            continue

        task = {
            "name": name,
            "id": str(uuid.uuid4()),
            "created_at": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            "status": "pending"
        }

        data.append(task)
        save_data(json_file, data)

        print("Task added successfully!")
        return


# VIEW TASKS
def view_tasks(data):

    if not data:
        print("No tasks found!")
        return

    print()
    print(pd.DataFrame(data))


# MARK TASK DONE
def mark_task_done(json_file, data):

    if not data:
        print("No tasks found!")
        return

    print()
    print(pd.DataFrame(data))

    try:
        num = int(input("\nEnter task number: ").strip())

        if not (0 <= num < len(data)):
            print("Invalid task number!")
            return

        if data[num]["status"] == "completed":
            print("Task already completed!")
            return

        data[num]["status"] = "completed"
        save_data(json_file, data)

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number!")


# DELETE TASK
def delete_task(json_file, data):

    if not data:
        print("No tasks found!")
        return

    print()
    print(pd.DataFrame(data))

    try:
        num = int(input("\nEnter task number: ").strip())

        if not (0 <= num < len(data)):
            print("Invalid task number!")
            return

        del data[num]
        save_data(json_file, data)

        print("Task deleted successfully!")

    except ValueError:
        print("Please enter a valid number!")


# MAIN
def main():

    print("Welcome to Simple CLI Todo App!")

    json_file = BASE_DIR / "data.json"
    data = load_data(json_file)

    while True:

        choice = menu()

        if choice == 1:
            add_task(json_file, data)

        elif choice == 2:
            view_tasks(data)

        elif choice == 3:
            mark_task_done(json_file, data)

        elif choice == 4:
            delete_task(json_file, data)

        else:
            print("Exiting...")
            break


main()