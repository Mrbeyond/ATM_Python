from termcolor import  colored
class UserInput:
    def __init__(self):
        pass
    
    def OUT(self,val, col):
        return print(colored(val, col))
    def validate(self, value):
        check = ('firstName', 'lastName', 'password', 'amountIn', 'amountOut', 'pin', 'accountType', 'int', 'accountNum')
        if value in check:
            collector = input('\n >>>')
            if check.index(value) < 2:
                if not collector.isalpha():
                    self.OUT('Sorry name can only contain alphabets', 'red')
                    return False
                else:
                    return collector
            elif check.index(value) == 2:
                if len(collector) < 8 or not collector.isalnum() :
                    self.OUT('Sorry password can only be alphanumeric and must be atleast 8 characters', 'red')
                    return False
                else:
                    return collector            
            elif check.index(value) > 2 and check.index(value) < 5:
                if not collector.isnumeric():
                    self.OUT('Sorry amount can only be numbers', 'red')
                    return False
                else:
                    return float(collector)
            elif check.index(value) == 7:
                if collector.isnumeric() and len(collector)==1:
                    return int(collector)
                else:
                    self.OUT('Sorry, invalid value was entered', 'red')
                    return False
            elif check.index(value) == 5:
                if len(collector ) == 4 and collector.isnumeric():
                    return int(collector)
                else:
                    self.OUT('Sorry Four digits pin is required', 'red')
                    return False
            elif check.index(value) == 6:
                if collector.isnumeric():
                    if len(collector ) == 1 and int(collector) >0 and int(collector) < 3:
                        return int(collector)
                    else:
                        self.OUT('Invalid key was entered', 'red')
                        return False
                else:
                    self.OUT('Number is required', 'red')
                    return False                    
                 
            else:
                if collector.isnumeric() and len(collector) == 10:
                    return (collector)
                else:
                    self.OUT('Invalid account number was provided', 'red')
                    return False
        else:
            self.OUT('Error!! Invalid value was entered, Hint internal', 'red')
            return False
    
# print(UserInput().validate('pin') )
