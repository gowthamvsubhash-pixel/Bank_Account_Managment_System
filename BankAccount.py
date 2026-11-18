from abc import ABC,abstractmethod

class BankAccount(ABC):

    # ee thazhe cheyth vechekkunna init functon ahn constructor
    def __init__(self):
        self.__balance = 0
        #self.account_name  = account_name
        #self.account_number = account_number
        #self.__balance = balance  # by adding two under scores we made it private(Encapsulation)

#ee init function upayogikkumpal ath end cheyyande avishyam onnum illa,
#athupole pass enna cammand kodukkunnath child class run cheyyan parent class il method 
# nokkumpol,ethelum method ippol run cheyyanda enn ondengil,avide parent class create cheyyumpol thanne pass koduthekkuaka.

    @abstractmethod #this method must be inhertited by the child class
    def calculate_interest(self):
        pass

    # it diplaying balance amount
    def display_balance(self):
        #we are displaying a private information.
        print(f"Account Balance is : {self.__balance} ")

    def get_balance(self):
        return self.__balance
    
# ivide thanne nokkiyal kahnam randinum pass koduthu karanam nilavil parentclass il
# athin prevarthi onnum illa ennal child class varumpol ath execute cheyyan ollath ahn.
# thats why it is typed earlier    
    
    
    def deposit(self,amount):
        if(amount>0):
            self.__balance = self.__balance + amount
            print(f"Deposited {amount} in your account, Your new balance is {self.__balance}")
        else:
            print("Deposit amount should be a  positive number")

    def withdraw(self,amount):
        if(amount>self.__balance):
            print("Insufficent Balance")
        elif(amount<=0):
            print("Please enter a valid amount !!!!!")
        elif(amount<=self.__balance):
            self.__balance = self.__balance - amount
            print(f"Amount of {amount},has been withdrwan and now your balance is {self.__balance}")
        print("************************************************")
        print("Thank u for visiting")    
