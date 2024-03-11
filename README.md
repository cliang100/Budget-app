**Budget App**

This is a simple budget app that allows you to create categories for tracking your expenses. It provides functionalities to deposit money, withdraw money, transfer money between categories, and generate a spending chart based on your expenses.

**Usage**

To use this app, follow these steps:

1. **Category Class**: The `Category` class is used to create categories for tracking expenses. Each category has a name and a ledger to record transactions.

    ```python
    class Category:
        def __init__(self, category):
            self.category = category
            self.ledger = []

        # Function to deposit money into the category
        def deposit(self, amount, description=''):
            self.ledger.append({"amount": amount, "description": description})

        # Function to withdraw money from the category
        def withdraw(self, amount, description=''):
            if self.check_funds(amount):
                self.ledger.append({"amount": -amount, "description": description})
                return True
            else:
                return False

        # Function to get the balance of the category
        def get_balance(self):
            balance = 0
            for item in self.ledger:
                balance += item["amount"]
            return balance

        # Function to transfer money between categories
        def transfer(self, amount, other_category):
            if self.check_funds(amount):
                self.withdraw(amount, f'Transfer to {other_category.category}')
                other_category.deposit(amount, f'Transfer from {self.category}')
                return True
            else:
                return False

        # Function to check if sufficient funds are available
        def check_funds(self, amount):
            return amount <= self.get_balance()

        # Function to display category details
        def __str__(self):
            title = f"{self.category.center(30, '*')}\n"
            items = ''
            total = 0
            for transaction in self.ledger:
                description = transaction['description'][:23].ljust(23)
                amount = '{:.2f}'.format(transaction['amount']).rjust(7)
                items += f'{description}{amount}\n'
                total += transaction['amount']
            total = 'Total: {:.2f}'.format(total)
            return title + items + total
    ```

2. **Create Spend Chart Function**: The `create_spend_chart` function generates a spending chart based on the expenses of different categories. It calculates the percentage spent in each category and visualizes it in the form of a chart.

3. **Example Usage**: An example usage of the budget app is provided at the end of the script. It demonstrates how to create categories, deposit money, withdraw money, transfer money between categories, print category details, and generate a spending chart.

4. **Customization**: You can customize the app by adding more functionalities or modifying existing ones according to your requirements.

**Note**: Ensure that you have Python installed on your system to run this app. You can execute the script directly to see the example usage.
