from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import json
from pathlib import Path

#base dir
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", 
    env_file_encoding="utf-8", 
    extra="ignore" )

    DISCORD_TOKEN: str
    APP_ID: str
    PUBLIC_KEY: str

    GOOGLE_CREDS_JSON: Optional[str] = None

    GOOGLE_SHEETS_CREDENTIALS_FILE: str = "google-credentials.json"
    GOOGLE_SHEETS_SPREADSHEET_NAME: str = "FinancialStatements"

settings = Settings()