from orator import  DatabaseManager, Model
class AppEloquent():
    def __init__(self):
        self.configuration = {'mysql':{'driver':'mysql','host': 'localhost','database': 'atm3',\
        'user': 'root','password': '', 'prefix': '' } }
        self.db = DatabaseManager(self.configuration)
        self.customer = self.db.table('customers')
        self.account = self.db.table('accounts')
        # self.first('id', 5)
        # self.first('type', 2)

    def first(self, identifier, data):
        mir = self.account.where(identifier, data).first()
        print(mir)
# AppEloquent()
    