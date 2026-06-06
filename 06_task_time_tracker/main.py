import time
from datetime import datetime
import pandas as pd


# MENU
def menu():
    while True:
        try:
            choice = int(input(
                "\n--- Task Time Tracker ---\n"
                "1. Start Task\n"
                "2. Track Time\n"
                "3. Stop Task\n"
                "4. Save Session\n"
                "5. Show History\n"
                "6. Exit\n: "
            ).strip())

            if choice in [1, 2, 3, 4, 5, 6]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# START TASK
def start_task():

    while True:

        title = input("Enter Task Title: ").strip()

        if not title:
            print("Task title cannot be empty!")
            continue

        return title


# SHOW HISTORY
def show_history(history):

    if not history:
        print("No history found!")
        return

    print()
    print(pd.DataFrame(history))


# MAIN
def main():

    task_running = False

    current_task = None

    start_timestamp = None
    created_at = None

    elapsed_time = 0

    history = []

    while True:

        choice = menu()

        # START TASK
        if choice == 1:

            if task_running:
                print("A task is already running!")
                continue

            current_task = start_task()

            task_running = True

            start_timestamp = time.time()

            created_at = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            print(
                f"Tracking started for '{current_task}'."
            )

        # TRACK TIME
        elif choice == 2:

            if not task_running:
                print("No active task!")
                continue

            elapsed = time.time() - start_timestamp

            print(f"Task: {current_task}")
            print(f"Elapsed Time: {elapsed:.2f} seconds")

        # STOP TASK
        elif choice == 3:

            if not task_running:
                print("No active task!")
                continue

            elapsed_time = time.time() - start_timestamp

            task_running = False

            print(f"Task: {current_task}")
            print(
                f"Final Time: {elapsed_time:.2f} seconds"
            )

            print("\nNow choose option 4 to save.")

        # SAVE SESSION
        elif choice == 4:

            if current_task is None:
                print("No session available!")
                continue

            if task_running:
                print("Stop the task first!")
                continue

            history.append({
                "task": current_task,
                "duration_seconds": round(
                    elapsed_time, 2
                ),
                "started_at": created_at,
                "ended_at": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            })

            print("Session saved successfully!")

            current_task = None
            start_timestamp = None
            created_at = None
            elapsed_time = 0

        # SHOW HISTORY
        elif choice == 5:

            show_history(history)

        # EXIT
        else:

            print("Exiting...")
            break


main()