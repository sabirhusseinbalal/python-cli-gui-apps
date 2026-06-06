import time
import os

# UTIL
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins:02}:{secs:02}"


# CORE TIMER ENGINE
def run_timer(label, seconds):
    try:
        while seconds > 0:
            clear()
            print("Press Ctrl+C to stop and return to menu\n")
            print(f"{label}")
            print(format_time(seconds))

            time.sleep(1)
            seconds -= 1

        print(f"\n{label} finished!")
        input("Press Enter to return to menu...")

    except KeyboardInterrupt:
        print("\n\nTimer stopped by user.")
        input("Press Enter to return to menu...")


# MENU
def menu():
    while True:
        try:
            choice = int(input(
                "\n--- Pomodoro System ---\n"
                "1. Pomodoro (25 min)\n"
                "2. Short Break (5 min)\n"
                "3. Long Break (15 min)\n"
                "4. Custom Timer\n"
                "5. Exit\n: "
            ).strip())

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# CUSTOM TIMER
def custom_timer():
    try:
        label = input("Enter timer label: ").strip()
        if not label:
            print("Label cannot be empty!")
            return

        seconds = int(input("Enter seconds: ").strip())
        if seconds <= 0:
            print("Invalid time!")
            return

        run_timer(label, seconds)

    except ValueError:
        print("Please enter valid number!")


# MAIN
def main():
    print("Pomodoro CLI Timer System")

    while True:
        choice = menu()

        if choice == 1:
            run_timer("Pomodoro Session", 25 * 60)

        elif choice == 2:
            run_timer("Short Break", 5 * 60)

        elif choice == 3:
            run_timer("Long Break", 15 * 60)

        elif choice == 4:
            custom_timer()

        else:
            print("Exiting...")
            break


main()