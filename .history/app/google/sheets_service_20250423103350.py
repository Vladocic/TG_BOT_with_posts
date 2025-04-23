import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_SHEET_ID

SERVICE_ACCOUNT_FILE = "credentials.json" 
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)


def get_sheet():
    creds = C.from_json_keyfile_name(SERVICE_ACCOUNT_FILE,SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open(GOOGLE_SHEET_ID).sheet1
    return sheet

def append_post_to_sheet(id:int, user_id:int, title:str, body:str):
    sheet.append_row([str(id), str(user_id), title, body])
