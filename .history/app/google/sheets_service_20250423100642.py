import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_SHEET_ID

SERVICE_ACCOUNT_FILE = "credentials.json" 



credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)