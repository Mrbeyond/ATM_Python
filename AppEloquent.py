from orator import  DatabaseManager, Model
class AppEloquent():
    def __init__(self):
        self.configuration = {'mysql':{'driver':'mysql','host': 'localhost','database': 'atm3',\
        'user': 'root','password': '', 'prefix': '' } }
        self.db = DatabaseManager(self.configuration)
        self.customer = self.db.table('customers')
        self.account = self.db.table('accounts')
        self.transaction = self.db.table('transactions')
        self.firstUser('id', 6)
        self.firstAccount('type', 2)
        self.statement('id', 1)

    def firstUser(self, identifier, data):
        return self.customer.where(identifier, data).first()
        # print(mir)
    def firstAccount(self, identifier, data):
        return self.account.where(identifier, data).first()
    def statement(self, identifier, data):
        return self.transaction.where(identifier, data).get()
        # allTransaction = self.transaction.where(identifier, data).get()
        # collector = ()
        # # print(collector, type(collector))
        # for x in allTransaction:
            
AppEloquent()
    