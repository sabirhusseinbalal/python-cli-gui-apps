from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import pandas as pd
import uuid
import json
import string

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"


# HELPERS
def clean_title(title: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    return title.lower().translate(translator).strip()


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_data():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)



# MENU
def menu():
    while True:
        try:
            choice = int(input(
                "\n--- Bookmark Manager ---\n"
                "1. Add Bookmark\n"
                "2. View Bookmarks\n"
                "3. Update Bookmark\n"
                "4. Delete Bookmark\n"
                "5. Exit\n: "
            ).strip())

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# ADD BOOKMARK
def add_bookmark(data):
    print("\n(Add 'q' to cancel)\n")

    while True:
        title = input("Title: ").strip().lower()
        if title == "q":
            return

        title = clean_title(title)
        if not title:
            print("Title cannot be empty!")
            continue

        category = input("Category: ").strip().lower()
        if category == "q":
            return

        if not category:
            print("Category cannot be empty!")
            continue

        url = input("URL: ").strip()
        if url == "q":
            return

        if url.startswith("www."):
            url = "https://" + url

        if not is_valid_url(url):
            print("Invalid URL!")
            continue

        bookmark = {
            "id": str(uuid.uuid4()),
            "title": title,
            "category": category,
            "url": url,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data.append(bookmark)
        save_data(data)

        print("Bookmark added successfully!")
        return



# VIEW BOOKMARKS
def view_bookmarks(data):
    if not data:
        print("No bookmarks found!")
        return

    print()
    print(pd.DataFrame(data))



# UPDATE BOOKMARK
def update_bookmark(data):
    if not data:
        print("No bookmarks found!")
        return

    print(pd.DataFrame(data))

    try:
        index = int(input("\nSelect bookmark number: ").strip())

        if not (0 <= index < len(data)):
            print("Invalid index!")
            return

        item = data[index]

        print("\nPress Enter to keep current value OR type 'n' to skip field\n")

        new_title = input(f"Title ({item['title']}): ").strip().lower()
        if new_title and new_title != "n":
            item["title"] = clean_title(new_title)

        new_category = input(f"Category ({item['category']}): ").strip().lower()
        if new_category and new_category != "n":
            item["category"] = new_category

        new_url = input(f"URL ({item['url']}): ").strip()
        if new_url and new_url != "n":
            if new_url.startswith("www."):
                new_url = "https://" + new_url

            if is_valid_url(new_url):
                item["url"] = new_url
            else:
                print("Invalid URL skipped!")

        item["last_updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_data(data)
        print("Bookmark updated successfully!")

    except ValueError:
        print("Please enter a valid number!")


# DELETE BOOKMARK
def delete_bookmark(data):
    if not data:
        print("No bookmarks found!")
        return

    print(pd.DataFrame(data))

    try:
        index = int(input("\nSelect bookmark number: ").strip())

        if not (0 <= index < len(data)):
            print("Invalid index!")
            return

        removed = data.pop(index)
        save_data(data)

        print(f"Deleted: {removed['title']}")

    except ValueError:
        print("Please enter a valid number!")


# MAIN
def main():
    print("Welcome to Bookmark Manager")

    data = load_data()

    while True:
        choice = menu()

        if choice == 1:
            add_bookmark(data)

        elif choice == 2:
            view_bookmarks(data)

        elif choice == 3:
            update_bookmark(data)

        elif choice == 4:
            delete_bookmark(data)

        else:
            print("Exiting...")
            break


main()