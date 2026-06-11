from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import json
import webbrowser
import string
import uuid
import random

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "links.json"


# HELPERS
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


def generate_code(data):
    """Generate unique short code like: a7k3, x9b2"""
    chars = string.ascii_lowercase + string.digits

    while True:
        code = "".join(random.choice(chars) for _ in range(5))
        if not any(item["code"] == code for item in data):
            return code
        
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)


# MENU
def menu():
    while True:
        try:
            choice = int(input(
                "\n--- URL Shortener ---\n"
                "1. Add URL\n"
                "2. View Links\n"
                "3. Open Link\n"
                "4. Delete Link\n"
                "5. Exit\n: "
            ))

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# CORE FEATURES
def add_url(data):

    url = input("URL: ").strip()
    if url == "q":
        return

    if url.startswith("www."):
        url = "https://" + url

    if not is_valid_url(url):
        print("Invalid URL!")
        return

    code = generate_code(data)

    item = {
        "id": str(uuid.uuid4()),
        "code": code,
        "url": url,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(item)
    save_data(data)

    print(f"\nShort URL created!")
    print(f"Code: {code}")
    print(f"Use this code to open the link.")


def view_links(data):
    if not data:
        print("No links found!")
        return

    print("\n--- Saved Links ---")
    for i, item in enumerate(data):
        print(f"{i}. [{item['code']}] → {item['url']}")


def open_link(data):
    if not data:
        print("No links found!")
        return

    code = input("\nEnter code: ").strip().lower()

    for item in data:
        if item["code"] == code:
            print(f"Opening: {item['url']}")
            webbrowser.open(item["url"])
            return

    print("Code not found!")


def delete_link(data):
    if not data:
        print("No links found!")
        return

    view_links(data)

    code = input("\nEnter code to delete: ").strip().lower()

    for i, item in enumerate(data):
        if item["code"] == code:
            removed = data.pop(i)
            save_data(data)
            print(f"Deleted: {removed['url']}")
            return

    print("Code not found!")


#  MAIN
def main():
    print("Welcome to CLI URL Shortener (Real Tool)")

    data = load_data()

    while True:
        choice = menu()

        if choice == 1:
            add_url(data)

        elif choice == 2:
            view_links(data)

        elif choice == 3:
            open_link(data)

        elif choice == 4:
            delete_link(data)

        else:
            print("Exiting...")
            break


main()