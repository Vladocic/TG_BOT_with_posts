import os
import json
import gspread
from google.oauth2 import service_account
from app.config import GOOGLE_SHEET_ID

def get_sheet():
    """
    Авторизуется через переменную окружения GOOGLE_CREDENTIALS
    и возвращает доступ к Google Таблице по ID.
    """
    credentials_raw = os.getenv("GOOGLE_CREDENTIALS")
    if not credentials_raw:
        raise ValueError("Переменная GOOGLE_CREDENTIALS не задана")

    # Преобразуем строку в словарь, заменив \\n на \n
    credentials_info = json.loads(credentials_raw.replace("\\n", "\n"))

    creds = service_account.Credentials.from_service_account_info(
        credentials_info,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    client = gspread.authorize(creds)
    return client.open_by_key(GOOGLE_SHEET_ID).sheet1