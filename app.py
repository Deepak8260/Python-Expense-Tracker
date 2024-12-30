import json
import os
from datetime import datetime

# Function to load expenses from a file
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    else:
        return []

# Function to save expenses to a file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Function to log a new expense
def log_expense(expenses):
    category = input("Enter the expense category: ")
    amount = float(input("Enter the amount: "))
    date = input("Enter the date (YYYY-MM-DD): ")

    expense = {
        "category": category,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)
    print(f"Expense of {amount} in category {category} added successfully.")
    save_expenses(expenses)

# Function to generate a report
def generate_report(expenses):
    category = input("Enter the category to filter (or leave blank for all): ")
    filtered_expenses = [expense for expense in expenses if (category == "" or expense['category'].lower() == category.lower())]
    
    total = 0
    for expense in filtered_expenses:
        total += expense['amount']
        print(f"{expense['date']} | {expense['category']} | {expense['amount']}")
    
    print(f"Total amount: {total}")

# Main menu for the user
def menu():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Application")
        print("1. Log Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            log_expense(expenses)
        elif choice == "2":
            generate_report(expenses)
        elif choice == "3":
            generate_report(expenses)
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()