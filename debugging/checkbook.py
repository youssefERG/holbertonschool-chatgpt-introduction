#!/usr/bin/python3
"""
Checkbook Management System
A simple command-line application to manage bank account deposits and withdrawals.
"""

class Checkbook:
    """
    A class to manage basic checkbook operations (deposit, withdraw, balance).

    Attributes:
        balance (float): Current account balance, initialized to 0.0
    """

    def __init__(self):
        """Initialize the checkbook with a balance of 0.0"""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the account.

        Parameters:
            amount (float): The amount to deposit. Must be positive.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Parameters:
            amount (float): The amount to withdraw. Must be positive and <= balance.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current account balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Prompt the user for a monetary amount with error handling.

    Keeps asking until the user enters a valid positive number.

    Parameters:
        prompt (str): The input prompt to display.

    Returns:
        float: A valid positive amount entered by the user.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Error: Amount must be positive. Please try again.")
                continue
            return amount
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")


def main():
    """
    Main function that runs the checkbook application loop.

    Allows users to perform deposit, withdraw, and balance check operations.
    Handles invalid commands and input errors gracefully.

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

            if action.lower() == 'exit':
                print("Thank you for using Checkbook. Goodbye!")
                break
            elif action.lower() == 'deposit':
                amount = get_valid_amount("Enter the amount to deposit: $")
                cb.deposit(amount)
            elif action.lower() == 'withdraw':
                amount = get_valid_amount("Enter the amount to withdraw: $")
                cb.withdraw(amount)
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()