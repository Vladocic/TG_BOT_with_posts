import os
from dotenv import load_dotenv

load_dotenv()

REQUIRED_VARS = {
    "BOT_TOKEN": None,
    "DATABASE_URL": None,
    "GOOGLE_SHEET_ID": None,
    "WEBHOOK_URL": None,
}

for key in REQUIRED_VARS:
    REQUIRED_VARS[key] = os.getenv(key)
    if REQUIRED_VARS[key] is None:
        raise ValueError(f"⚠️ Переменная окружения {key} не установлена в .env")

BOT_TOKEN = REQUIRED_VARS["BOT_TOKEN"]
DATABASE_URL = REQUIRED_VARS["DATABASE_URL"]
GOOGLE_SHEET_ID = REQUIRED_VARS["GOOGLE_SHEET_ID"]
# WEBHOOK_URL = REQUIRED_VARS["WEBHOOK_URL"]
WEBHOOK_URL = ""
