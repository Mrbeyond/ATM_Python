from termcolor import  colored
class UserInput:
    def __init__(self):
        pass
    
    def OUT(self,val, col):
        return print(colored(val, col))
    def validate(self, value):
        check = ('firstName', 'lastName', 'password', 'amountIn', 'amountOut', 'pin', 'accountType', 'int', 'accountNum')
        proceed = True
        if value in check:
            collector = input('\n >>>')
            if check.index(value) < 2:
                if not collector.isalpha():
                    proceed = False
                    self.OUT('Sorry name can only contain alphabets', 'red')
                else:
                    return collector
            elif check.index(value) == 2:
                if len(collector) < 8 or not collector.isalnum() :
                    proceed = False
                    self.OUT('Sorry password can only be alphanumeric and must be atleast 8 characters', 'red')
                else:
                    return collector            
            elif check.index(value) > 2 and check.index(value) < 5:
                if not collector.isnumeric():
                    proceed = False
                    self.OUT('Sorry amount can only be numbers', 'red')
                else:
                    return float(collector)
            elif check.index(value) == 7:
                if collector.isnumeric() and len(collector)==1:
                    return int(collector)
                else:
                    proceed = False
                    self.OUT('Sorry, invalid value was entered', 'red')
                 
            else:
                if collector.isnumeric():                
                    if value == 'accountType':
                        if  len(collector ) == 1 and int(collector) >0 and int(collector) < 3:
                            return int(collector)
                        else:
                            proceed = False
                            self.OUT('Invalid key was entered', 'red')
                    elif value == 'accountNum':
                        if  len(collector ) != 10:
                            proceed = False
                            self.OUT('Sorry Four digits pin is required', 'red')
                        else:
                            return (collector)
                        
                    else:
                        if len(collector ) != 4 and value == 'pin':
                            proceed = False
                            self.OUT('Sorry Four digits pin is required', 'red')
                        else:
                            return int(collector)
                else:
                    proceed = False
                    self.OUT('Sorry Invalid values are entered', 'red')
        else:
            proceed = False
            self.OUT('Error!! Invalid value is entered, Hint internal', 'red')
        return proceed
    
# print(UserInput().validate('pin') )
