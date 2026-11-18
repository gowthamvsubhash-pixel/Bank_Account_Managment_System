

# we are reffering to the original file ,ennale parent file ayi connect cheyth ithin work akan pattu.
from BankAccount import BankAccount


class SavingsAccount(BankAccount):


    def calculate_interest(self):
        #fetching the balance and then calculating interest as 5% of the balance.
        interest = (self.get_balance()) * 5/100
        print(f"your interest on savings Account is -:  {interest}")
        return interest





