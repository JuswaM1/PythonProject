import csv
from datetime import datetime


EXPENSE_FILE = "expenses.csv"


def log_expense():
    try:
        amount = float(input("Enter the amount (₱): "))
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
        description = input("Enter a description: ")

        
        with open(EXPENSE_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount, category, description])

        print("Expense logged successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")


def generate_report():
    try:
        with open(EXPENSE_FILE, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

        if not expenses:
            print("No expenses logged yet.")
            return

        total_expense = 0
        category_totals = {}

        
        for expense in expenses:
            amount = float(expense[1])
            category = expense[2]
            total_expense += amount
            category_totals[category] = category_totals.get(category, 0) + amount

        print("\n--- Expense Report ---")
        print(f"Total Expenses: ₱{total_expense:.2f}")
        print("Expenses by Category:")
        for category, total in category_totals.items():
            print(f"  {category}: ₱{total:.2f}")
    except FileNotFoundError:
        print("No expenses logged yet. Start by logging an expense!")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Log an Expense")
        print("2. Generate Report")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            log_expense()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
