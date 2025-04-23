import os
import json
import gspread
from google.oauth2 import service_account
from app.config import GOOGLE_SHEET_ID

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_sheet():
    """
    Авторизуется через переменную окружения GOOGLE_CREDENTIALS
    и возвращает доступ к Google Таблице по ID.
    """
    raw_credentials = os.getenv("GOOGLE_CREDENTIALS")
    if not raw_credentials:
        raise ValueError("❌ Переменная GOOGLE_CREDENTIALS не установлена")

    info = json.loads(raw_credentials)
    credentials = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)

    client = gspread.authorize(credentials)
    sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1
    return sheet