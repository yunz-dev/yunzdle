# app.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from fastapi import FastAPI

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Yunzdle Database").sheet1
data = sheet.get_all_records()
print(data)
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

