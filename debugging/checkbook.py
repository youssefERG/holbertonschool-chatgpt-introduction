class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a valid positive amount into the checkbook.
        """
        if amount <= 0:
            print("Amount must be positive to deposit.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a valid positive amount from the checkbook if sufficient funds exist.
        """
        if amount <= 0:
            print("Amount must be positive to withdraw.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Displays the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting checkbook. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
