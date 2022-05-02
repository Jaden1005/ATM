class ATM (object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number
    
    def CashWithdrawl(self):
        print("Withdraw cash")
    
    def BalanceEnquiry(self):
        print("Balance")
    
myaccount=ATM("6891","1849")
print(myaccount.card_number)
myaccount.CashWithdrawl()
myaccount.BalanceEnquiry()