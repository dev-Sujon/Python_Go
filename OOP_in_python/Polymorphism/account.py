##################################################################################################
#Design a Bank class with a method calculate_interest.
# Create subclasses SavingsAccount and LoanAccount that have their own interest calculation logic.
###################################################################################################

class Bank:
    def calculate_interest(self):
        pass
class SavingsAccount(Bank):
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return 0.03 * self.balance  # Example: 3% interest rate

class LoanAccount(Bank):
    def __init__(self, principal):
        self.principal = principal

    def calculate_interest(self):
        return 0.08 * self.principal  # Example: 8% interest rate for loans

# Example usage
savings_account = SavingsAccount(10000)
loan_account = LoanAccount(50000)

print("Savings Account Interest:", savings_account.calculate_interest())
print("Loan Account Interest:", loan_account.calculate_interest())
