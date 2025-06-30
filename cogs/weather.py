import discord
from discord.ext import commands
import aiohttp
import os

API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name="weather")
    async def get_weather(self, ctx, zip_code: str):
        """Gets the weather for a ZIP code (US only)."""
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={API_KEY}&units=imperial"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    await ctx.send("Failed to get weather data. Check the ZIP code.")
                    print(resp.status)
                    return

                data = await resp.json()

                # Parse data
                city = data["name"]
                weather_desc = data["weather"][0]["description"].title()
                temp = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]

                embed = discord.Embed(
                    title=f"Weather in {city} ({zip_code})",
                    description=weather_desc,
                    color=discord.Color.blue()
                )
                embed.add_field(name="Temperature", value=f"{temp}°F (Feels like {feels_like}°F)", inline=False)
                embed.add_field(name="Humidity", value=f"{humidity}%", inline=False)

                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Weather(bot))
