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
                "\n1. Add Habit\n"
                "2. View Habits\n"
                "3. Mark Habit Done\n"
                "4. Delete Habit\n"
                "5. Exit\n: "
            ).strip())

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
            pass

        print("Invalid Choice!")


# ADD HABIT
def add_habit(json_file, data):

    while True:
        name = input("Enter Habit name (or 'q'): ").strip()

        if name.lower() == "q":
            return

        if not name:
            print("Habit name cannot be empty!")
            continue

        habit = {
            "name": name,
            "id": str(uuid.uuid4()),
            "history": [str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))],
            "completed": 0
        }

        data.append(habit)
        save_data(json_file, data)

        print("Habit added successfully!")
        return


# VIEW HABITS
def view_habits(data):

    if not data:
        print("No habits found!")
        return

    print()
    df = pd.DataFrame(data)
    print(df[["name", "completed", "history"]])


# MARK HABIT DONE
def mark_habit_done(json_file, data):

    if not data:
        print("No habits found!")
        return

    print()
    df = pd.DataFrame(data)
    print(df[["name", "completed"]])

    try:
        num = int(input("\nEnter habit number: ").strip())

        if not (0 <= num < len(data)):
            print("Invalid habit number!")
            return
        
        data[num]["history"].append(
            str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )

        data[num]["completed"] += 1
        save_data(json_file, data)

        print("Today's Habit counted!")

    except ValueError:
        print("Please enter a valid number!")


# DELETE HABIT
def delete_habit(json_file, data):

    if not data:
        print("No habits found!")
        return

    print()
    print(pd.DataFrame(data))

    try:
        num = int(input("\nEnter habit number: ").strip())

        if not (0 <= num < len(data)):
            print("Invalid habit number!")
            return

        del data[num]
        save_data(json_file, data)

        print("Habit deleted successfully!")

    except ValueError:
        print("Please enter a valid number!")


# MAIN
def main():

    print("Habit Tracker")
    print("\nDaily Habits...\n")

    json_file = BASE_DIR / "data.json"
    data = load_data(json_file)

    while True:

        choice = menu()

        if choice == 1:
            add_habit(json_file, data)

        elif choice == 2:
            view_habits(data)

        elif choice == 3:
            mark_habit_done(json_file, data)

        elif choice == 4:
            delete_habit(json_file, data)

        else:
            print("Exiting...")
            break


main()