from UserInput import UserInput
from BankingBasic import BankingBasic
from AppEloquent import AppEloquent
class Operation(UserInput, BankingBasic ):
    def __init__(self):
        BankingBasic.__init__(self)
        self.Eloquent = AppEloquent()
        # print(self.Eloquent.configuration)
        self.name = 'ade'
        self.defaultAmount = (1000,2000,5000,10000,20000,50000,100000,'Other')
        self.displayAmount = ("#1,000","#2,000","#5,000","#10,000","#20,000","#50,000","#100,000",'Other')
        

    def enterPassword(self):
        print("\33[32m Please enter your Password \33[0m ")
        password = self.validate('password')
        if password:
            return password
            # 
        else:
            return self.handleError(self.enterPassword,)
            
    def enterName(self, namer):
        print(f"\33[32m Please enter your {namer} \33[0m ")    
        firstName = self.validate(namer)
        if firstName:
            return firstName
            # 
        else:
            return self.handleError(self.enterName(namer), self.enterName(namer))
        
    def enterAccountType(self):
        print("\33[32m Please enter your desired account type \33[0m ")
        print("\33[36m 1 Curent\n 2 Savings \33[0m")
        accType = self.validate('accountType')
        if accType:
            return accType
        else:
            return self.handleError(self.enterAccountType,)
            
    def displayWelcome(self):
        print(" \33[32m YOU WELCOME TO BEYOND'S ATM APP \33[0m ")
        route= input("\33[36m 1  Login \n 2  Register \n 3  Exit \33[0m \n >>>")
        if route in (('1', '2', '3')):
            if route == "3":
                print("\33[37m Thanks for your time. I hope we served you well? \33[0m")
                exit()
            else:
                if route =="1":
                    self.logUserIn()
                else:
                    pass
        else:
            print("\33[31m Invalid value was entered \33[0m")
            return self.handleError(self.displayWelcome)
    
    def logUserIn(self):
        print("You are about to Login into you account, please provide your firstname and password \n")
        password = self.enterPassword()
        print(f"password is {password}")
        
        firstName = self.enterName('firstName')
        print(f"firstName is {firstName}")
         
        if password and firstName:
            self.login((firstName, password))
            
        else:
            print('\33[31m Sorry, unable to process your details, please try again \33[0m')
            return self.handleError(self.logUserIn,)
        
    def signUserUp(self):
        print("You are about to Register an Account with us \n")
        password = self.enterPassword(recurse)
        print(f"password is {password}")
        
        firstName = self.enterName('firstName')
        print(f"firstName is {firstName}")
        
        lastName =  self.enterName('lastName')
        print(f"lastName is {lastName}")
        
        accType = self.enterAccountType(recurse)
        print(f"account type is {accType}")
            
        if password and firstName and lastName and accType:
            GO = {'password':password, "firstName": firstName, "lastName": lastName, "type": accType}
            return GO
        else:
            print('\33[31m Sorry, unable to process your provided details, please try again \33[0m')
            return self.handleError(self.signUserUp,)
    
                
            
    def intro(self):
        introOptions = ("Withdraw Money", "Balance Enquiry", "Transfer", "Deposit Money", "Transaction History", "Bill Pay", "Setting", "Exit")
        print("\n Please select a transaction \n")
        for index, option in enumerate(introOptions):
            print(f"\33[36m {index+1}    {option} \33[0m")
        print(" \n \33[35m Enter the value here\33[0m")
        inputIndex = self.validate('int')
        if inputIndex in ((1,2,3,4,5,6,7,8)):
            return inputIndex
        else:
            print("\33[31m Invalid value was entered \33\[0m ")
            self.handleError(self.intro)
            
        
            
            
    def displayWithdraw(self):
        print("\n Please select an amount \n")
        for index, option in enumerate(self.defaultAmount):
            print(f"\33[36m {index+1}     {self.displayAmount[index]} \33[0m")
            
        inputIndex = self.validate('int')
        if inputIndex:
            if inputIndex == 8:
                print('Enter the amount you want to withdraw')
                amount = self.validate('amountOut')
                if amount:
                    return amount
                else:
                    print("\33[31m Invalid value was entered \33\[0m ")
                    self.handleError(self.displayWithdraw, self.intro)
            elif inputIndex <8 and inputIndex> 0:
                return self.defaultAmount[inputIndex-1]
            else:
                print("\33[31m Invalid value was entered \33\[0m ")
                self.handleError(self.displayWithdraw, self.intro)            
        else:
            print("\33[31m Invalid value was entered \33\[0m ")
            self.handleError(self.displayWithdraw, self.intro)
            
    def displayTransfer(self):
        print("\nYou are about to make a Transfer\n  Please enter an option below:\n")
        route= input("\33[36m 1 Same bank \n 2 Other banks \33[0m \n >>>")
        if route in (('1', '2')):
            print("\33[36m Enter the amount here \33[0m ")       
            amount = self.validate('amountIn')
            if amount:
                return amount
            else:
                print("\33[31m Invalid value was entered \33\[0m ")
                self.handleError(self.displayTransfer, self.intro)
                
        else:
            print("\33[31m Invalid value was entered \33\[0m ")
            self.handleError(self.displayTransfer, self.intro)
    
    
        
    def displayDeposit(self):        
        print(" \33[35m \nYou are about to make a Deposit into your account\n  Please enter the amount:\n \33[0m")
        amount = self.validate('amountIn')
        if amount:
            return amount
        else:
            print("\33[31m Invalid value was entered \33\[0m ")
            self.handleError(self.displayDeposit, self.intro)
        

    def inputAmount(self):
        print("\33[36m Enter the amount here \33[0m ")       
        amount = self.validate('amountOut')
        if amount:
            return amount
        else:
            pass
        
    def handleError(self, method1, method2=lambda : print('')):
        route= input("\33[35m 1 Try again \n 2 Main Menu \n 0 Exit \33[0m \n >>>")
        if route in (('1', '2', '0')):
            if route == '1':
                return  method1()
            elif route =="2":
                method2()
                return
            else:
                print("\33[33m Thanks for your time. I hope we served you well? \33[0m")
                return   exit()
        else:
            print("\33[31m Invalid value was entered \33[0m ")
            return  self.handleError(method1)
Operation().displayWelcome()      
# Operation().intro()
# Operation().displayWithdraw()
# Operation().inputAmount()
# Operation().displayTransfer()
# Operation().logUserIn()