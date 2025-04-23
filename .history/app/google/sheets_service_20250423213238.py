import gspread
from google.oauth2 import service_account
from app.config import GOOGLE_SHEET_ID

def get_sheet():
    """
    Авторизация через секретный файл в Render:
    /etc/secrets/google_credentials.json
    """
    creds = service_account.Credentials.from_service_account_file(
        "/etc/secrets/google_credentials.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    client = gspread.authorize(creds)
    return client.open_by_key(GOOGLE_SHEET_ID).sheet1