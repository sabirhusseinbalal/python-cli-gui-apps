import uuid
from datetime import datetime
import pandas as pd


# MENU
def menu():
    while True:
        try:
            choice = int(
                input(
                    "\n1. Earning\n"
                    "2. Expense\n"
                    "3. Check Balance\n"
                    "4. Update Transaction\n"
                    "5. Exit\n: "
                ).strip()
            )

            if choice in [1, 2, 3, 4, 5]:
                return choice

        except ValueError:
            pass

        print("Invalid choice!")


# ADD TRANSACTION
def add_transaction():
    while True:
        try:
            name = input("Enter Text (or 'q'): ").strip()

            if name.lower() == "q":
                return None

            if not name:
                print("Text cannot be empty!")
                continue

            amount = int(input("Enter Amount: ").strip())

            if amount <= 0:
                print("Please enter a valid amount!")
                continue

            return name, amount

        except ValueError:
            print("Please enter a valid number!")


# UPDATE TRANSACTION
def update_transaction(transactions, num):
    while True:
        try:
            amount = int(input("Enter New Amount: ").strip())

            if amount <= 0:
                print("Please enter a valid amount!")
                continue

            transaction = transactions[num]

            return (
                amount,
                transaction["status"],
                transaction["amount"]
            )

        except ValueError:
            print("Please enter a valid number!")


# SHOW TRANSACTIONS
def show_transactions(transactions):
    print()
    print(pd.DataFrame(transactions))


# MAIN
def main():

    print("Expense Tracker")

    balance = 0
    earnings = 0
    expenses = 0

    transactions = []

    while True:

        choice = menu()

        # EARNING
        if choice == 1:

            result = add_transaction()

            if result is None:
                continue

            name, amount = result

            earnings += amount
            balance += amount

            transaction = {
                "text": name,
                "amount": amount,
                "datetime": str(datetime.now()),
                "id": str(uuid.uuid4()),
                "status": "Earning"
            }

            transactions.append(transaction)

            print("Earning transaction added successfully!")

        # EXPENSE
        elif choice == 2:

            result = add_transaction()

            if result is None:
                continue

            name, amount = result

            expenses += amount
            balance -= amount

            transaction = {
                "text": name,
                "amount": amount,
                "datetime": str(datetime.now()),
                "id": str(uuid.uuid4()),
                "status": "Expense"
            }

            transactions.append(transaction)

            print("Expense transaction added successfully!")

        # BALANCE
        elif choice == 3:

            if balance < 0:
                print("\nCurrent balance is negative.")
            else:
                print("\nCurrent balance is positive.")

            print(f"Balance : {balance}$")
            print(f"Earnings: {earnings}$")
            print(f"Expenses: {expenses}$")

        # UPDATE / DELETE
        elif choice == 4:

            if not transactions:
                print("No transactions found!")
                continue

            show_transactions(transactions)

            while True:
                try:
                    num = int(input("\nEnter transaction number: ").strip())

                    if not (0 <= num < len(transactions)):
                        print("Invalid transaction number!")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid number!")

            while True:
                try:
                    action = int(
                        input(
                            "\n1. Edit Transaction\n"
                            "2. Delete Transaction\n: "
                        )
                    )

                    if action in [1, 2]:
                        break

                except ValueError:
                    pass

                print("Invalid choice!")

            # DELETE
            if action == 2:

                if transactions[num]["status"] == "Earning":

                    earnings -= transactions[num]["amount"]
                    balance -= transactions[num]["amount"]

                else:

                    expenses -= transactions[num]["amount"]
                    balance += transactions[num]["amount"]

                del transactions[num]

                print("Transaction deleted successfully!")

            # EDIT
            else:

                amount, status, prev_amount = update_transaction(
                    transactions,
                    num
                )

                if status == "Earning":

                    earnings -= prev_amount
                    balance -= prev_amount

                    transactions[num]["amount"] = amount

                    earnings += amount
                    balance += amount

                else:

                    expenses -= prev_amount
                    balance += prev_amount

                    transactions[num]["amount"] = amount

                    expenses += amount
                    balance -= amount

                print("Transaction updated successfully!")

        # EXIT
        else:
            print("Exiting...")
            break


main()