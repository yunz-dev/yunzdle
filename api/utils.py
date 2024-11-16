import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

def singleton(cls):
    # dict to store instance of classes
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        # return the instance
        return instances[cls]
    
    return get_instance

# enum for datasets
@singleton
class Datasets:
    def __init__(self):
        self.test = 'test'
        self.meta = 'meta'
        self.pip = 'pinpoint'
        self.con = 'connections'
        self.wor = 'wordle'
        self.emo = 'emoji'

# database class
@singleton
class SheetDataBase:
    def __init__(self, database: str):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        self.name = database
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = {
            #'meta': self.client.open(database).worksheet('meta'),
            #'test' : self.client.open(database).worksheet('test'),
            # 'connections' : self.client.open(database).sheet3,
            # 'emoji' : self.client.open(database).sheet4,
            # 'pinpoint' : self.client.open(database).sheet5,
            # 'wordle' : self.client.open(database).sheet6,
        }
        self.data = {
            # 'meta': self.sheet['meta'].get_all_records(),
            # 'test' : self.sheet['test'].get_all_records(),
            # 'connections' : this.sheet['connections'].get_all_records(),
            # 'emoji' : this.sheet['emoji'].get_all_records(),
            # 'pinpoint' : this.sheet['pinpoint'].get_all_records(),
            # 'wordle' : this.sheet['wordle'].get_all_records(),
        }

     #updates the data for 1 sheet   
    def update(self, sheet: str):
        if sheet not in self.sheet:
            self.sheet[sheet] = self.client.open(self.name).worksheet(sheet)
        self.data[sheet] = self.sheet[sheet].get_all_records()

    # queries a sheet for data
    def query(self, sheet):
        return self.data[sheet]





s = Datasets()
s2 = Datasets()
print(s, s2, s is s2)
db = SheetDataBase('Yunzdle Database')
db2 = SheetDataBase('Yunzdle Database')
print(db is db2)
db.update(s.test)
db.update(s.meta)
print(db.query(s.test))
print(db.query(s.meta))



