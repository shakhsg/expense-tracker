# 💰 Expense Tracker

A clean, beginner-friendly **CLI Expense Tracker** built with Python.  
Track your daily expenses, edit or delete records, and view monthly summary reports — all from your terminal.

> ✅ Built with pure Python · OOP design · JSON file storage · No database needed

---

## 📁 Project Structure

```
expense-tracker/
│
├── main.py             # Entry point — runs the CLI menu
├── expense.py          # Expense class (data model)
├── expense_tracker.py  # ExpenseTracker class (core logic)
├── expenses.json       # Data file (auto-created, do not delete)
└── README.md           # This file
```

---

## ✨ Features

| Feature                  | Description                                      |
|--------------------------|--------------------------------------------------|
| ➕ Add Expense            | Record a new expense with date, category, and amount |
| ✏️ Edit Expense           | Update any existing expense by its ID            |
| 🗑️ Delete Expense         | Remove an expense after confirming               |
| 📋 View All Expenses      | See all expenses in a formatted table with total |
| 📊 Monthly Summary        | View category-wise spending for any month        |
| 💾 Auto Save & Load       | Data is saved to JSON and loaded on startup      |

---

## 🚀 How to Run

### 1. Prerequisites

Make sure you have **Python 3.6+** installed.

```bash
python3 --version
```

### 2. Navigate to the project folder

```bash
cd path/to/expense-tracker
```

### 3. Run the program

```bash
python3 main.py
```

You'll see the main menu in your terminal:

```
========================================
       💰 EXPENSE TRACKER
========================================
  1. Add Expense
  2. Edit Expense
  3. Delete Expense
  4. View All Expenses
  5. Monthly Summary Report
  6. Exit
========================================
```

---

## 🧪 Example Usage

### Adding an Expense

```
Enter your choice (1-6): 1

--- ➕ Add New Expense ---
  Date (YYYY-MM-DD): 2025-03-18
  Category (e.g. Food, Transport): Food
  Description: Lunch at cafe
  Amount ($): 12.50

✅ Expense added successfully! (ID: 1)
```

### Viewing All Expenses

```
Enter your choice (1-6): 4

======================================================================
ID     Date         Category        Description               Amount
======================================================================
1      2025-03-18   Food            Lunch at cafe             $  12.50
2      2025-03-18   Transport       Grab ride to office       $   8.00
======================================================================
TOTAL                                                          $  20.50
======================================================================
```

### Monthly Summary

```
Enter your choice (1-6): 5

--- 📊 Monthly Summary Report ---
  Enter year (e.g. 2025): 2025
  Enter month number (1-12): 3

=============================================
  📊 Monthly Summary — 2025-03
=============================================
  Category             Total
  -----------------------------------
  Food                 $     12.50
  Transport            $      8.00
  -----------------------------------
  GRAND TOTAL          $     20.50
=============================================
```

---

## 🗂️ Expense Fields

| Field         | Type    | Description                        |
|---------------|---------|------------------------------------|
| `id`          | int     | Auto-assigned unique identifier    |
| `date`        | string  | Format: `YYYY-MM-DD`               |
| `category`    | string  | e.g. Food, Transport, Health       |
| `description` | string  | Short note about the expense       |
| `amount`      | float   | Amount spent (must be > 0)         |

---

## 🏗️ OOP Design

```
expense.py
└── class Expense
    ├── __init__()       → Creates an expense object
    ├── to_dict()        → Converts to dict for JSON saving
    ├── from_dict()      → Creates object from saved JSON data
    └── __str__()        → Pretty-prints the expense

expense_tracker.py
└── class ExpenseTracker
    ├── load_expenses()       → Reads from expenses.json
    ├── save_expenses()       → Writes to expenses.json
    ├── add_expense()         → Adds a new expense
    ├── edit_expense()        → Updates an existing expense
    ├── delete_expense()      → Removes an expense
    ├── view_all_expenses()   → Prints all expenses
    └── view_monthly_summary()→ Prints monthly category totals

main.py
└── main()                    → Menu loop and user input handling
```

---

## 🛡️ Input Validation

- Dates must follow `YYYY-MM-DD` format
- Amounts must be positive numbers
- Category and description cannot be blank
- Deletion requires confirmation (`y/n`)
- Invalid menu choices show a helpful error message

---

## 💡 Suggested Expense Categories

- Food
- Transport
- Shopping
- Health
- Entertainment
- Utilities
- Rent
- Education
- Other

---

## 📌 Notes

- Data is automatically saved after every operation
- The `expenses.json` file is created automatically on first run
- No internet connection or external libraries required

---

## 👨‍💻 Author

Built as a portfolio project to demonstrate:
- Python OOP fundamentals
- File I/O with JSON
- CLI application design
- Clean, readable code structure

---

*Made with ❤️ using pure Python*
