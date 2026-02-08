from discord.ext import commands
import discord
from datetime import datetime
from  app.utils.validators import validate_financial_data

class DiscordBot(commands.Bot):
    def __init__(self, sheet_service):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.sheets = sheet_service
        @self.event
        async def on_message(message):
            # Jangan respon jika pesan dari bot itu sendiri
            if message.author == self.user:
                return

            print(f"Pesan masuk: {message.content}") # Ini akan muncul di terminal Anda
            
            # PENTING: Harus ada baris ini agar command (!catat) tetap berjalan
            await self.process_commands(message)
        @self.command()
        async def record(ctx, *, message: str):
            """Records a message with a timestamp to Google Sheets."""
            print(ctx)
            try:
                # parse data
                data = [i.strip() for i in message.split(",")]
                valid_categories = self.sheets.get_valid_expense_categories()
                valid_sources = self.sheets.get_valid_sources()

                is_valid, clean_data, error_msg = validate_financial_data(data, valid_categories, valid_sources)
                if not is_valid:
                    return await ctx.send(f"Error: {error_msg}")
                tgl = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                row_data = [tgl, *clean_data, ctx.author.name]

                # Append to Google Sheets
                self.sheets.append_row(row_data)
                await ctx.send("Data recorded successfully.")
            except Exception as e:
                await ctx.send(f"Error: {str(e)}")

