# main.py
# This is the entry point of the Expense Tracker application.
# It shows the menu and handles user interactions.

from expense_tracker import ExpenseTracker


def print_menu():
    """Displays the main menu options to the user."""
    print("\n" + "=" * 40)
    print("       💰 EXPENSE TRACKER")
    print("=" * 40)
    print("  1. Add Expense")
    print("  2. Edit Expense")
    print("  3. Delete Expense")
    print("  4. View All Expenses")
    print("  5. Monthly Summary Report")
    print("  6. Exit")
    print("=" * 40)


def get_valid_amount(prompt):
    """
    Asks the user to enter an amount and keeps asking until
    a valid positive number is provided.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        float: A valid positive amount.
    """
    while True:
        try:
            amount = float(input(prompt).strip())
            if amount <= 0:
                print("❌ Amount must be greater than zero. Try again.")
            else:
                return amount
        except ValueError:
            print("❌ Invalid amount. Please enter a number (e.g. 12.50).")


def get_valid_date(prompt):
    """
    Asks the user to enter a date in YYYY-MM-DD format.
    Keeps asking until a valid format is provided.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        str: A valid date string in YYYY-MM-DD format.
    """
    while True:
        date = input(prompt).strip()
        # Check that the date has the right format: YYYY-MM-DD
        parts = date.split("-")
        if (
            len(parts) == 3
            and len(parts[0]) == 4
            and len(parts[1]) == 2
            and len(parts[2]) == 2
            and all(part.isdigit() for part in parts)
        ):
            return date
        else:
            print("❌ Invalid date format. Please use YYYY-MM-DD (e.g. 2025-03-18).")


def get_valid_int(prompt):
    """
    Asks the user to enter a valid integer.
    Keeps asking until a valid integer is provided.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        int: A valid integer.
    """
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("❌ Please enter a whole number.")


def handle_add(tracker):
    """Handles the 'Add Expense' flow."""
    print("\n--- ➕ Add New Expense ---")
    date = get_valid_date("  Date (YYYY-MM-DD): ")
    category = input("  Category (e.g. Food, Transport): ").strip()
    description = input("  Description: ").strip()
    amount = get_valid_amount("  Amount ($): ")

    # Validate that category and description are not empty
    if not category or not description:
        print("❌ Category and description cannot be empty.")
        return

    tracker.add_expense(date, category, description, amount)


def handle_edit(tracker):
    """Handles the 'Edit Expense' flow."""
    print("\n--- ✏️  Edit Expense ---")
    expense_id = get_valid_int("  Enter the ID of the expense to edit: ")
    print("  Enter new values (leave blank to cancel):")
    date = get_valid_date("  New Date (YYYY-MM-DD): ")
    category = input("  New Category: ").strip()
    description = input("  New Description: ").strip()
    amount = get_valid_amount("  New Amount ($): ")

    if not category or not description:
        print("❌ Category and description cannot be empty.")
        return

    success = tracker.edit_expense(expense_id, date, category, description, amount)
    if not success:
        print(f"❌ No expense found with ID {expense_id}.")


def handle_delete(tracker):
    """Handles the 'Delete Expense' flow."""
    print("\n--- 🗑️  Delete Expense ---")
    expense_id = get_valid_int("  Enter the ID of the expense to delete: ")

    # Ask for confirmation before deleting
    confirm = input(f"  Are you sure you want to delete expense ID {expense_id}? (y/n): ").strip().lower()
    if confirm == "y":
        success = tracker.delete_expense(expense_id)
        if not success:
            print(f"❌ No expense found with ID {expense_id}.")
    else:
        print("  Deletion cancelled.")


def handle_monthly_summary(tracker):
    """Handles the 'Monthly Summary' flow."""
    print("\n--- 📊 Monthly Summary Report ---")
    year = get_valid_int("  Enter year (e.g. 2025): ")
    month = get_valid_int("  Enter month number (1-12): ")

    if month < 1 or month > 12:
        print("❌ Month must be between 1 and 12.")
        return

    tracker.view_monthly_summary(year, month)


def main():
    """
    Main function — runs the program loop.
    Creates the tracker, then shows the menu in a loop
    until the user chooses to exit.
    """
    print("\nWelcome to Expense Tracker! 💰")
    print("Your personal finance manager.\n")

    # Create the tracker (this also loads existing data from the file)
    tracker = ExpenseTracker()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            handle_add(tracker)
        elif choice == "2":
            handle_edit(tracker)
        elif choice == "3":
            handle_delete(tracker)
        elif choice == "4":
            tracker.view_all_expenses()
        elif choice == "5":
            handle_monthly_summary(tracker)
        elif choice == "6":
            print("\n👋 Goodbye! Your expenses have been saved.\n")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")


# This ensures main() only runs when this file is executed directly,
# not when it's imported by another module.
if __name__ == "__main__":
    main()
