# expense_tracker.py
# This file contains the ExpenseTracker class.
# It manages all operations: add, edit, delete, view, and file handling.

import json
import os
from expense import Expense


# The name of the file where expenses will be saved
DATA_FILE = "expenses.json"


class ExpenseTracker:
    """
    Manages a collection of expenses.

    Responsibilities:
    - Load and save expenses to/from a JSON file
    - Add, edit, delete, and display expenses
    - Generate monthly summary reports
    """

    def __init__(self):
        # This list stores all Expense objects in memory
        self.expenses = []
        # Load any existing expenses from the file when the program starts
        self.load_expenses()

    # ──────────────────────────────────────────────
    # FILE HANDLING
    # ──────────────────────────────────────────────

    def load_expenses(self):
        """
        Loads expenses from the JSON file into memory.
        If the file doesn't exist or is empty, starts with an empty list.
        """
        if not os.path.exists(DATA_FILE):
            # No file yet — start fresh
            self.expenses = []
            return

        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                # Convert each dictionary back into an Expense object
                self.expenses = [Expense.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            # File is corrupted or has wrong format — start fresh
            print("⚠️  Warning: Could not read expenses file. Starting fresh.")
            self.expenses = []

    def save_expenses(self):
        """
        Saves all current expenses to the JSON file.
        Converts each Expense object to a dictionary first.
        """
        with open(DATA_FILE, "w") as file:
            # Convert each Expense object to a dict, then save as JSON
            data = [expense.to_dict() for expense in self.expenses]
            json.dump(data, file, indent=4)

    # ──────────────────────────────────────────────
    # ID MANAGEMENT
    # ──────────────────────────────────────────────

    def _get_next_id(self):
        """
        Generates the next unique ID for a new expense.
        It finds the highest existing ID and adds 1.
        """
        if not self.expenses:
            return 1
        return max(expense.expense_id for expense in self.expenses) + 1

    def _find_expense_by_id(self, expense_id):
        """
        Searches for an expense by its ID.

        Args:
            expense_id (int): The ID to search for.

        Returns:
            Expense or None: The matching Expense object, or None if not found.
        """
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense
        return None

    # ──────────────────────────────────────────────
    # CORE FEATURES
    # ──────────────────────────────────────────────

    def add_expense(self, date, category, description, amount):
        """
        Creates a new expense and adds it to the list.
        Automatically assigns a unique ID.

        Args:
            date (str): Date in YYYY-MM-DD format.
            category (str): Expense category.
            description (str): Brief description.
            amount (float): Amount spent.
        """
        new_id = self._get_next_id()
        new_expense = Expense(new_id, date, category, description, amount)
        self.expenses.append(new_expense)
        self.save_expenses()
        print(f"\n✅ Expense added successfully! (ID: {new_id})")

    def edit_expense(self, expense_id, date, category, description, amount):
        """
        Edits an existing expense by its ID.

        Args:
            expense_id (int): The ID of the expense to edit.
            date (str): New date.
            category (str): New category.
            description (str): New description.
            amount (float): New amount.

        Returns:
            bool: True if edit was successful, False if ID not found.
        """
        expense = self._find_expense_by_id(expense_id)
        if expense is None:
            return False

        # Update the expense fields
        expense.date = date
        expense.category = category
        expense.description = description
        expense.amount = amount
        self.save_expenses()
        print(f"\n✅ Expense ID {expense_id} updated successfully!")
        return True

    def delete_expense(self, expense_id):
        """
        Deletes an expense by its ID.

        Args:
            expense_id (int): The ID of the expense to delete.

        Returns:
            bool: True if deletion was successful, False if ID not found.
        """
        expense = self._find_expense_by_id(expense_id)
        if expense is None:
            return False

        self.expenses.remove(expense)
        self.save_expenses()
        print(f"\n✅ Expense ID {expense_id} deleted successfully!")
        return True

    def view_all_expenses(self):
        """
        Displays all expenses in a formatted table.
        Shows a message if there are no expenses yet.
        """
        if not self.expenses:
            print("\n📭 No expenses found. Start by adding one!\n")
            return

        print("\n" + "=" * 70)
        print(f"{'ID':<6} {'Date':<12} {'Category':<15} {'Description':<25} {'Amount':>8}")
        print("=" * 70)

        for expense in self.expenses:
            print(
                f"{expense.expense_id:<6} "
                f"{expense.date:<12} "
                f"{expense.category:<15} "
                f"{expense.description:<25} "
                f"${expense.amount:>7.2f}"
            )

        # Show total at the bottom
        total = sum(e.amount for e in self.expenses)
        print("=" * 70)
        print(f"{'TOTAL':<55} ${total:>7.2f}")
        print("=" * 70 + "\n")

    def view_monthly_summary(self, year, month):
        """
        Displays a summary report for a specific month and year.
        Shows totals grouped by category.

        Args:
            year (int): The year (e.g. 2025).
            month (int): The month number (1–12).
        """
        # Filter expenses that match the given year and month
        month_str = f"{year}-{month:02d}"  # e.g. "2025-03"
        monthly_expenses = [
            e for e in self.expenses if e.date.startswith(month_str)
        ]

        if not monthly_expenses:
            print(f"\n📭 No expenses found for {month_str}.\n")
            return

        # Group amounts by category
        category_totals = {}
        for expense in monthly_expenses:
            category = expense.category
            category_totals[category] = category_totals.get(category, 0) + expense.amount

        print(f"\n{'=' * 45}")
        print(f"  📊 Monthly Summary — {month_str}")
        print(f"{'=' * 45}")
        print(f"  {'Category':<20} {'Total':>10}")
        print(f"  {'-' * 35}")

        for category, total in sorted(category_totals.items()):
            print(f"  {category:<20} ${total:>9.2f}")

        grand_total = sum(category_totals.values())
        print(f"  {'-' * 35}")
        print(f"  {'GRAND TOTAL':<20} ${grand_total:>9.2f}")
        print(f"{'=' * 45}\n")
