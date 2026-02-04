

class Bank:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
        
    def deposit(self):
        self.balance+=int(input('Enter the amount to deposit: '))
        print('Deposit is sucessful')
        self.bankFees()
    def withdrawal(self):
        
        draw=int(input('Enter the  amount to withdraw: '))
        if self.balance >= draw:
         self.balance-=draw
         print('Withdrawal is sucessful')
        self.bankFees()

    def bankFees(self):
        print('Each withdrawl will deduct 5% of your original balance')
        self.balance*=0.95
        
    def display(self):
        print('Account Number : ',self.accountNumber)
        print('Account Name : ',self.name)
        print('Account Balance : ',self.balance,'$')
        
    
        
        
obj = Bank(20215,'Darwin',7500)
obj.display()
