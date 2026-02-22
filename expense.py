import csv
from datetime import datetime

file_name = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    description = input("Enter description: ")

    with open(file_name, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!\n")

def view_expenses():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            print("\n--- All Expenses ---")
            for row in reader:
                print(row)
            print()
    except FileNotFoundError:
        print("No expenses found!\n")

def monthly_summary():
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0
    category_totals = {}

    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                date, amount, category, description = row
                if date[5:7] == month and date[:4] == year:
                    total += float(amount)
                    category_totals[category] = category_totals.get(category, 0) + float(amount)

        print("\n--- Monthly Summary ---")
        print("Total Spending:", total)
        print("Category-wise Breakdown:")
        for cat, amt in category_totals.items():
            print(f"{cat}: {amt}")
        print()

    except FileNotFoundError:
        print("No expenses found!\n")

def menu():
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.\n")

menu()
