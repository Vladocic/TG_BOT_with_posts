import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL=https://yourdomain.com/webhook
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/dbname
GOOGLE_SHEET_ID=your_google_sheet_id



if BOT_TOKEN is None:
    raise ValueError('No Bot_token in file')
