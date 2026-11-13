import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist yet."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    """Prompts the user for expense details and saves them to the CSV."""
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Category (e.g., Food, Transport, Bills): ").strip().capitalize()
    description = input("Description: ").strip()
    
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, f"{amount:.2f}"])
    
    print(f"Saved: {description} ({category}) - {amount:.2f}\n")

def view_summary():
    """Reads the CSV and displays all expenses plus the total spent."""
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return

    total = 0.0
    print("\n--- Expense History ---")
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        rows = list(reader)

        if not rows:
            print("No expenses recorded yet.\n")
            return

        for row in rows:
            date, category, description, amount = row
            print(f"{date} | {category:<12} | {description:<20} | {float(amount):.2f}")
            total += float(amount)

    print("-" * 55)
    print(f"Total Spent: {total:.2f}\n")

def main():
    initialize_file()
    while True:
        print("1. Add Expense")
        print("2. View Expenses & Total")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
