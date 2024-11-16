# app.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from fastapi import FastAPI
import google.generativeai as genai
import os

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Yunzdle Database").sheet1
data = sheet.get_all_records()
print(data)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("what's 1+1")
print(response.text)
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

