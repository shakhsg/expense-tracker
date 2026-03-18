# expense.py
# This file defines the Expense class.
# Each expense object holds one expense entry's data.


class Expense:
    """
    Represents a single expense.

    Attributes:
        expense_id (int): Unique identifier for the expense.
        date (str): Date of the expense in YYYY-MM-DD format.
        category (str): Category of the expense (e.g. Food, Transport).
        description (str): Short description of what was spent on.
        amount (float): Amount of money spent.
    """

    def __init__(self, expense_id, date, category, description, amount):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def to_dict(self):
        """
        Converts the Expense object into a dictionary.
        This is used when saving data to the JSON file.
        """
        return {
            "id": self.expense_id,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }

    @staticmethod
    def from_dict(data):
        """
        Creates an Expense object from a dictionary.
        This is used when loading data from the JSON file.

        Args:
            data (dict): A dictionary with expense fields.

        Returns:
            Expense: A new Expense object.
        """
        return Expense(
            expense_id=data["id"],
            date=data["date"],
            category=data["category"],
            description=data["description"],
            amount=data["amount"]
        )

    def __str__(self):
        """
        Returns a nicely formatted string representation of the expense.
        This is displayed when printing expenses in the terminal.
        """
        return (
            f"[ID: {self.expense_id}] "
            f"{self.date} | "
            f"{self.category:15} | "
            f"{self.description:25} | "
            f"${self.amount:.2f}"
        )
