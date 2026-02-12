class Bank():
    bank_name="sbi"
    ifsc_code=12345
    manager="Bharath"
    min_balance=1000
    
    def __init__(self,name,phone,account_no,balance):
        self.name=name
        self.phone=phone
        self.account_no=account_no
        self.balance=balance

    def deposit_money(self,amount):
        self.balance+=amount
        print("Deposited",amount)
        print("Bank Balance after depositing:",self.balance)

    def withdraw_money(self,amount):
        if self.balance>0 and self.balance>=Bank.min_balance:
            self.balance-=amount
            print("withdrawed amount:",amount)
            print("Balance remaining:",self.balance)
        else:
            print("InSufficient Balance")
        
    def display_details(self):
        print("Name:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)

    #class method
    @classmethod
    def update_minbalance(cls,new_balance):
        cls.min_balance=new_balance
        print("Updated minimum balance to:",new_balance)

b1=Bank("Siri",9988776655,5689,5000)
b1.deposit_money(1000)
b1.withdraw_money(2000)
b1.display_details()
Bank.update_minbalance(2000)
