from CurrentAccount import currentaccount
from SavingsAccount import SavingsAccount
#create an object of current account

ba1 = SavingsAccount()
ca1 = currentaccount()

# # inkane cheyyumbol ivide () ee coloumn kodukkal
# ca1.dummy()
# ca1.deposit(1000)
# #print(f"balance amount is :{ca1.__balance}")  #this and the one below this are almost same activity.but because it is encapslated
# it cannot be accesed in this way


# # To display the balance use the functions from the parent class.
ca1.display_balance()  


#cannot bedone because variable is protected from being accesed from outside

ca1.display_balance()
ca1.deposit(40000)
ca1.display_balance()
ca1.deposit(-200)
ca1.withdraw(50000)
ca1.display_balance()
ca1.display_balance()


ba1.display_balance()
ba1.deposit(40000)
ba1.display_balance()
ba1.deposit(-200)
ba1.withdraw(50000)
ba1.display_balance()

ca1.calculate_interest()
ba1.calculate_interest()





