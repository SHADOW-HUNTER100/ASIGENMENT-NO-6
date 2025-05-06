# Creating a class called Bank
class Bank:
    # Class variable
    bank_name = "National Bank"

    # Class method to change bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Method to display bank name
    def show_bank(self):
        print("Bank Name:", self.bank_name)

# Creating two objects of the Bank class
customer1 = Bank()
customer2 = Bank()

# Displaying bank name from both objects
customer1.show_bank()
customer2.show_bank()

# Changing bank name using class method
Bank.change_bank_name("Global Trust Bank")

# Displaying bank name again to show change
customer1.show_bank()
customer2.show_bank()
