import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
# WEBHOOK_URL=https://yourdomain.com/webhook
DATABASE_URL = os.getenv("DATABASE_URL")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")



if BOT_TOKEN is None:
    raise ValueError('No Bot_token in file')
if DATABASE_URL is None:
    raise ValueError('No DATABASE_URL in file')
if GOOGLE_SHEET_ID is None:
    raise ValueError('No GOOGLE_SHEET_ID in file')
if WEBHOOK_URL is None:
    raise ValueError('No Bot_token in file')

