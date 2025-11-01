import random
import os
class bank_account():
    def __init__(self,name,balance=0):
        self.name=name
        self.__account_no=random.randint(1000,9999)
        self.__balance=balance
    def deposit(self,amount):
        try:
            if amount<0:
                raise ValueError("ERROR!!!!.... Enter amount in positve form")
            self.__balance+=amount
        except ValueError as e:
            print(e)
    def withdraw(self,amount):
        try:
            if amount<0:
                raise ValueError("ERROR!!!!.... Enter amount in positive form")
            if amount>self.__balance:
                raise ValueError("ERROR!!!!.... Insufficient Balnace")
            self.__balance-=amount
        except ValueError as e:
            print(e)
    def check_balance(self):
        return self.__balance
    def check__account_no(self):
        return f"Your account number is {self.__account_no}"
    def bank_detials(self):
        print(f"Account holder name is       : {self.name}")
        print(f"Your account number is       : {self.__account_no}")
        print(f"Your current bank balance is : ₹{self.__balance}")
    def data_save(self):
        try: 
            with open("account.txt","a") as file:
                file.write(f"Account holder name is : {self.name}\nYour account number is : {self.__account_no}\nYour current bank balance is : {self.__balance}\n")
        except FileNotFoundError:
            print("File not found")  


class saving_account(bank_account):
    def __init__(self,name,balance=0,interest_rate=5):
        super().__init__(name,balance)
        self.interest_rate=interest_rate
    def calculate_rate(self):
        a=super().check_balance()
        interest=a*(self.interest_rate/100)
        print(f"Balance after applying interest :{interest}")


class Current_account(bank_account):
    def __init__(self, name, balance=0,limit=2000):
        super().__init__(name, balance)
        self.limit=limit
    def calculate_rate(self):
        print(f"Current account have no interest rate")


def load_account():
    print("Loading saved data........")
    if os.path.exists("account.txt"):
        with open("account.txt","r") as file:
            data=file.readlines()
            if not data:
                print("No account saved.......")
            for i in data:
                print(i)
                
            
print("******SMART BANK SYSTEM********")
load_account()
try:
    name=input("Enter Account Holder Name : ")
    print("Choose your account type")
    print("1. Saving Account")
    print("2. Current Account")
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        account=saving_account(name)
    elif choice==2:
        account=Current_account(name)
    else:
        raise ValueError("Invalid Choice!")
    while True:
        print("/n----MENU-------")
        print("1. Deposit Money")
        print("2. Withdraw Money") 
        print("3. Show Account Info")
        print("4. Calculate Interest")
        print("5. Save & Exit")
        option=int(input("Enter Your Choice (1-5) : "))
        if option==1:
            try:
                amount=float(input("Enter your amount : "))
                account.deposit(amount)
            except ValueError:
                print("Enter valid amount")
        elif option==2:
            try:
                amount=float(input("Enter your amount : "))
                account.withdraw(amount)
            except ValueError:
                print("Enter valid amount")               
        elif option==3:
            account.bank_detials()
        elif option==4:
            account.calculate_rate()
        elif option==5:
            account.data_save()
            print("Data Saved.......................")
            break
        else:
            print("Enter Valid Option :")
except ValueError as e:
    print("Error!!!!!!!!...",e)
except Exception as e:
    print("Unexpected Error!!!!!.........")
        
                
                