import pyperclip


# MENU
def menu():
    while True:
        try:
            choice = int(input(
                "\n--- Clipboard Manager ---\n"
                "1. Copy Text\n"
                "2. Paste Clipboard\n"
                "3. Show Clipboard\n"
                "4. Clear Clipboard\n"
                "5. Exit\n: "
            ).strip())

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# COPY TEXT
def copy_text():
    try:
        text = input("Enter text to copy: ").strip()

        if not text:
            print("Text cannot be empty!")
            return

        pyperclip.copy(text)
        print("Text copied to clipboard!")

    except Exception as e:
        print(f"Error: {e}")


# SHOW CLIPBOARD
def show_clipboard():
    try:
        text = pyperclip.paste()

        if not text:
            print("Clipboard is empty.")
            return

        print("\n--- Clipboard Content ---")
        print(text)

    except Exception as e:
        print(f"Error: {e}")


# PASTE CLIPBOARD (simulate use)
def paste_clipboard():
    try:
        text = pyperclip.paste()

        if not text:
            print("Clipboard is empty.")
            return

        print("\nPasted from clipboard:")
        print(text)

    except Exception as e:
        print(f"Error: {e}")


# CLEAR CLIPBOARD
def clear_clipboard():
    try:
        pyperclip.copy("")
        print("Clipboard cleared!")

    except Exception as e:
        print(f"Error: {e}")


# MAIN
def main():
    while True:
        choice = menu()

        if choice == 1:
            copy_text()

        elif choice == 2:
            paste_clipboard()

        elif choice == 3:
            show_clipboard()

        elif choice == 4:
            clear_clipboard()

        else:
            print("Exiting...")
            break


main()