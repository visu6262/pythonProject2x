class Bank():
    def __init__(self):
        self.balance=0
        self._p_balance=1000
    def deposit_bank(self,amount):
        self.balance = self.balance+amount
        print("Enter Deposit amount is :",amount)
    def _withdraw_bank(self,amount):
        self.balance = self.balance-amount
        print("Enter Withdrawal amount :",amount)

    def __shown_amount_bank(self):
        print("You r Bank Balance is:",self.balance)

    def bank_banlance_approval(self,is_approval):
        if is_approval:
            return (self.__shown_amount_bank())
        else:
            print("u r not auth person")

    def bank_manager_withdraw_approval(self,amount):
        self._withdraw_bank(amount=amount)

    def p_balance(self):
        print("private balance is :",self._p_balance)

hdfc=Bank()
hdfc.deposit_bank(1000)
hdfc.bank_manager_withdraw_approval(599)
hdfc.bank_banlance_approval(True)
hdfc.p_balance()

print("-----------")

sbi=Bank()
sbi.deposit_bank(5000)
sbi.bank_manager_withdraw_approval(650)
sbi.bank_banlance_approval(True)
sbi.p_balance()

print("-----------")

yes=Bank()
yes.deposit_bank(100)
yes.bank_manager_withdraw_approval(16)
yes.bank_banlance_approval(True)
yes.p_balance()