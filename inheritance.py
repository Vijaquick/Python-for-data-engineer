class bankaccount():
    def __init__(self,account_id,name):
        self.account_id=account_id
        self.name=name
    def account_details(self):
        print(f"your account_id:{self.account_id} and account holder name:{self.name}")
        
class country(bankaccount):
    
    def __init__(self,country_name,account_id,name):
        self.country_name=country_name
        bankaccount.__init__(self,account_id,name)
    
    def country_info(self):
        print(f"this account created from:{self.country_name}")


class current_account(country):
    def __init__(self,country_name,account_id,name,deposit):
        self.deposit = deposit
        bankaccount.__init__(self,account_id,name)
        country.__init__(self,country_name,account_id,name)
    
    def current_deposit(self):
        print(f"current account deposit amount:{self.deposit}")


class saving_account(current_account):
    def __init__(self,deposit_amount,country_name,account_id,name,deposit):
        self.deposit_amount=deposit_amount
        country.__init__(self,country_name,account_id,name)
    def deposit(self):
        print(f"you have deposited={self.deposit_amount}")
    
    def full_account_details(self):
        bankaccount.account_details(self)
        country.country_info(self)

cus1=saving_account(1000,7665554,"vijaquick","india",2000)

cus1.deposit()

