class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.category}')
            other_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
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

def create_spend_chart(categories):
    # Calculate total withdrawals for each category
    total_withdrawals = {category.category: sum(transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0) for category in categories}
    
    # Calculate total spent across all categories
    total_spent = sum(total_withdrawals.values())

    # Calculate percentage spent for each category
    percentages = {category: int((total_withdrawals[category] / total_spent) * 100) for category in total_withdrawals}

    chart = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + '| '
        for percentage in percentages.values():
            if percentage >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    
    # Add the x-axis and category labels
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'
    max_len = max(len(category) for category in total_withdrawals)
    for i in range(max_len):
        chart += '     '
        for category in total_withdrawals:
            if i < len(category):
                chart += category[i] + '  '
            else:
                chart += '   '
        chart += '\n'

    return chart

if __name__ == '__main__':
    # Create categories
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")
    
    # Deposit initial amounts
    food.deposit(300, "deposit")
    clothing.deposit(100, "deposit")
    auto.deposit(50, "deposit")
    
    # Withdraw amounts to achieve the desired split
    food.withdraw(180, "groceries")  # 60% of total spending
    clothing.withdraw(60, "shirt")   # 20% of total spending
    auto.withdraw(30, "fuel")        # 10% of total spending
    
    # Transfer some amount between categories
    food.transfer(20, clothing)
    
    # Print the details of each category
    print(food)
    print(clothing)
    print(auto)
    
    # Print the spend chart
    categories = [food, clothing, auto]
    print(create_spend_chart(categories))