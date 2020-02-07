from UserInput import UserInput
from BankingBasic import BankingBasic
class Operation(UserInput, BankingBasic ):
    def __init__(self):
        BankingBasic.__init__(self)
        self.name = 'ade'
        self.defaultAmount = (1000,2000,5000,10000,20000,50000,100000,'Other')
        self.displayAmount = ("#1,000","#2,000","#5,000","#10,000","#20,000","#50,000","#100,000",'Other')
        
    def displayWelcome(self):
        # # self.login(('beyond', '12345678'))
        print(self.signUserUp())
        return
        print(" \33[32m YOU WELCOME TO BEYOND'S ATM APP \33[0m ")
        route= input("\33[36m 1  Login \n 2  Register \n 3  Exit \33[0m \n >>>")
        if route in (('1', '2', '3')):
            print(route)
        else:
            print("\33[31m Invalid value was entered \33[0m")
            self.handleError(self.displayWelcome)
    def logUserIn(self):
        # password =
        print("\33[32m Please enter your Password \33[0m ")
        password = self.validate('password')
        if not password:
            self.handleError(self.logUserIn)
        print("\33[32m Please enter your firstName \33[0m ")    
        firstName = self.validate('firstName')
        if not firstName:
            self.handleError(self.logUserIn)            
        if password and firstName:
            GO = {'password':password, "firstName": firstName}
            return GO
        else:
            return False
        
    def signUserUp(self):
        print("You are about to Register an Account with us \n")
        
        print("\33[32m Please enter your Password \33[0m ")
        password = self.validate('password')
        if not password:
            self.handleError(self.signUserUp)
            
        print("\33[32m Please enter your firstName \33[0m ")
        firstName = self.validate('firstName')
        if not firstName:
            self.handleError(self.signUserUp)
            
        print("\33[32m Please enter your Lastname \33[0m ")
        lastName = self.validate('lastName')
        if not lastName:
            self.handleError(self.signUserUp)
        
        print("\33[32m Please enter your desired account type \33[0m ")
        print("\33[36m 1 Curent\n 2 Savings \33[0m")
        accType = self.validate('accountType')
        if not accType:
            self.handleError(self.signUserUp)
            
        if password and firstName and lastName and accType:
            GO = {'password':password, "firstName": firstName, "lastName": lastName, "type": accType}
            return GO
        else:
            return False
    
    def handleError(self, method1, method2=print):
        route= input("\33[35m 1 Try again \n 2 Main Menu \n 0 Exit \33[0m \n >>>")
        if route in (('1', '2', '0')):
            if route == '1':
                method1()
            elif route =="2":
                method2()
            else:
                print("\33[37m Thanks for your time. I hope we served you well? \33[0m")
                exit()
        else:
            print("Invalid value was entered")
            self.handleError(method1)
        
        
        
            
    def intro(self):
        introOptions = ("Withdraw Money", "Balance Enquiry", "Transfer", "Deposit Money", "Transaction History", "Bill Pay", "Setting")
        print("\n Please select a transaction \n")
        for index, option in enumerate(introOptions):
            print(f"\33[36m {index+1}    {option} \33[0m")
        print(" \n \33[35m Enter the value here >>>\33[0m")
            
            
    def displayWithdraw(self):
        print("\n Please select an amount \n")
        for index, option in enumerate(self.defaultAmount):
            print(f"\33[36m {index+1}     {self.displayAmount[index]} \33[0m")
            
        inputIndex = self.validate('int')
        if inputIndex:
            if inputIndex == 8:
                print('Enter the amount you want to withdraw')
                self.inputAmount()
                # amount = self.validate('amountOut')
            elif inputIndex <8 and inputIndex> 0:
                print(f" {self.defaultAmount[inputIndex-1]} is amount")
            else:
                print("error3")
            
        else:
            print('error2')
            
    def displayTransfer(self):
        print("\nYou are about to make a Transfer\n  Please enter an option below:\n")
        route= input("\33[36m 1 Same bank \n 2 Other banks \33[0m \n >>>")
        if route in (('1', '2')):
            print(route)
        else:
            print("Invalid value was entered")
    
    
        
    def displayDeposit(self):
        
        print("\nYou are about to make a Deposit into your account\n  Please enter the amount:\n")
          
        

    def inputAmount(self):
        print("\33[36m Enter the amount here")       
        amount = self.validate('amountOut')
        if amount:
            print(f"{amount} is amount")
        else:
            print("error");
    
        
    
        
# Operation().displayWelcome()      
# Operation().intro()
# Operation().displayWithdraw()
# Operation().inputAmount()
# Operation().displayTransfer()
# Operation().logUserIn()