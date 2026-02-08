import gspread
from oauth2client.service_account import ServiceAccountCredentials
from app.core.config import settings
import json
from pathlib import Path

class GoogleSheetsService:
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        # Load credentials from the specified JSON file
        file_path = Path(settings.GOOGLE_SHEETS_CREDENTIALS_FILE)
        if settings.GOOGLE_CREDS_JSON:
            creds_dict = json.loads(settings.GOOGLE_CREDS_JSON)
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

        elif file_path.exists():
            creds = ServiceAccountCredentials.from_json_keyfile_name(settings.GOOGLE_SHEETS_CREDENTIALS_FILE, scope)
        self.client = gspread.authorize(creds) 
        self.sheet = self.client.open(settings.GOOGLE_SHEETS_SPREADSHEET_NAME)
        self.main_sheet = self.sheet.worksheet("raw_data")  # Assuming we're working with the first sheet

    def get_valid_expense_categories(self):
        """Fetches valid categories from the Google Sheet."""
        settings_sheet = self.sheet.worksheet("Settings")
        categories = settings_sheet.col_values(2)[2:]  # Assuming categories are in the second column of Settings sheet
        return categories

    def get_valid_sources(self):
        """Fetches valid sources from the Google Sheet."""
        settings_sheet = self.sheet.worksheet("Settings")
        sources = settings_sheet.col_values(3)[2:]  # Assuming sources are in the third column of Settings sheet
        return sources

    def append_row(self, row_data):
        """Appends a row of data to the Google Sheet."""
        self.main_sheet.append_row(row_data)