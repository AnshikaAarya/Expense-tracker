
import datetime

# Expense class to store individual expense records
class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

# Function to add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (e.g., food, rent, entertainment): ")
        date_input = input("Enter date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        expenses.append(Expense(amount, category, date))
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")

# Function to view expenses by month and category
def view_monthly_expenses(expenses):
    try:
        month_input = input("Enter the month to view expenses (YYYY-MM): ")
        year, month = map(int, month_input.split('-'))
        monthly_expenses = {}
        
        # Loop through expenses and sum up by category for the chosen month
        for expense in expenses:
            if expense.date.year == year and expense.date.month == month:
                if expense.category in monthly_expenses:
                    monthly_expenses[expense.category] += expense.amount
                else:
                    monthly_expenses[expense.category] = expense.amount
        
        # Display the monthly expense breakdown
        if monthly_expenses:
            print(f"\nExpense summary for {month_input}:")
            for category, total in monthly_expenses.items():
                print(f"{category.capitalize()}: Rs.{total:.2f}")
        else:
            print(f"No expenses found for {month_input}.")
    
    except ValueError:
        print("Invalid input. Please enter the month in YYYY-MM format.")

# Main program loop
def main():
    expenses = []  # List to store all expenses
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add a new expense")
        print("2. View monthly expenses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_monthly_expenses(expenses)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()