from fastapi import FastAPI
import asyncio
from app.services.google_sheets import GoogleSheetsService
from app.services.discord_bot import DiscordBot
from app.core.config import settings

app = FastAPI(title="Financial Statement Bot")

sheet_service = GoogleSheetsService()
discord_bot = DiscordBot(sheet_service=sheet_service)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(discord_bot.start(settings.DISCORD_TOKEN))

@app.get("/health")
def health_check():   
    return {"status": "running", "bot": discord_bot.user.name if discord_bot.user else "offline","database": settings.GOOGLE_SHEETS_SPREADSHEET_NAME}