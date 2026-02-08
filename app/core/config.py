from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

#base dir
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore" )

    DISCORD_TOKEN: str
    APP_ID: int
    PUBLIC_KEY: str
    GOOGLE_SHEETS_CREDENTIALS_FILE: str = str(BASE_DIR / "google-credentials.json")
    GOOGLE_SHEETS_SPREADSHEET_NAME: str = "FinancialStatements"

settings = Settings()