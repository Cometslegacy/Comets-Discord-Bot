import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user} and are now online!')

# Load cogs
@bot.event
async def setup_hook():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and not filename.startswith("_"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            
bot.run(TOKEN)
