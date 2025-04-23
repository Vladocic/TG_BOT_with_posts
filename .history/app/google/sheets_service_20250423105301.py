import gspread
from google.oauth2.service_account import Credentials
from app.config import GOOGLE_SHEET_ID

SERVICE_ACCOUNT_FILE = "app/google/credentials.json" 
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def get_sheet():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes= SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open(GOOGLE_SHEET_ID).sheet1
    return sheet
