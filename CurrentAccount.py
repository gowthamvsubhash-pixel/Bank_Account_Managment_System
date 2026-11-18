from BankAccount import BankAccount
# inkane ahn orr file vera orr file nte child ahnenn kodukkunnath.


# The concept used here is "INHERITENCE" , we inhert methods and properties 
# of parent class

class currentaccount(BankAccount):


    def calculate_interest(self):
        interest = 0
        #self.get_balance()
        print(f"your interest on current Account is  -: {interest}")
        return interest



