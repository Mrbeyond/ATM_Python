from orator import  DatabaseManager, Model
from Operation import Operation
class App(Operation):
    def __init__(self):
        Operation.__init__(self)
        self.configuration = {'mysql':{'driver':'mysql','host': 'localhost','database': 'atm3',\
        'user': 'root','password': '', 'prefix': '' } }
        self.db = DatabaseManager(self.configuration)
        self.customer = self.db.table('customers')
        self.account = self.db.table('accounts')

    def tt(self):
        mir = self.account.where('id', 1).count()
        print(mir)
App().tt()
    