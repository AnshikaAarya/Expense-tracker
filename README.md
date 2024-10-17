
#Expense Tracker 

A simple Python-based expense tracker that helps you manage your income and expenses effectively. Track your daily, weekly, or monthly expenses, and keep a record of your financial activities in an organized way.

## Features

- Add, update, and delete expenses
- Track income and expenses by categories (e.g., groceries, bills, entertainment)
- View a summary of total expenses and income
- Generate reports for a specific time period (daily, weekly, monthly)
- Store data in CSV/JSON for easy access and editing
- User-friendly CLI (Command Line Interface)

## Requirements

- Python 3.x
- (Optional) Libraries: `pandas` for CSV manipulation, `matplotlib` for visualization

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AnshikaAarya/expense-tracker.git
cd expense-tracker
```

2. (Optional) Install additional dependencies if needed:

```bash
pip install pandas matplotlib
```

## Usage

1. Run the program:

```bash
python3 expense_tracker.py
```

2. Follow the prompts to:

- Add a new expense or income
- View your current expense history
- Generate reports for specific time periods

3. Example prompts:

```bash
Choose an option:
1. Add Expense
2. View Expenses
3. Generate Report
4. Exit

Enter the amount: 50
Enter category (e.g., groceries, rent, entertainment): groceries
Enter date (YYYY-MM-DD): 2024-10-17
Expense added successfully!
```

## Data Storage

By default, expenses are stored in a `expenses.csv` file (or `expenses.json` if using JSON). You can easily modify this file to view or back up your data.

## Sample Features

1. **Add Expenses**: Record daily expenses with details like amount, category, and date.
2. **View Expenses**: List all recorded expenses in a structured table format.
3. **Generate Reports**: Get a breakdown of your expenses and income over a specific time period, categorized for better analysis.
4. **Delete or Update Expenses**: Modify your existing records.

## Example Output

```bash
Date         Category     Amount
2024-10-15   Groceries    $50
2024-10-16   Transport    $20
----------------------------
Total Expenses: $70
```

## Customization

- **Categories**: Add your own categories for tracking expenses.
- **Data Storage**: Change data storage from CSV to a database like SQLite for more robust storage.

## Future Improvements

- Add a graphical user interface (GUI) for ease of use
- Integration with budgeting or financial planning tools
- Sync data across devices

