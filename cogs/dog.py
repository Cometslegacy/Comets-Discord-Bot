from discord.ext import commands
import discord
import aiohttp

class Dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                if resp.status != 200:
                    await ctx.send("Could not find Doggo :(")
                    return

                data = await resp.json()
                image_url = data["message"]

                embed = discord.Embed(
                    title="Random Dog!",
                    description="Doggo",
                    color=discord.Color.green()
                )
                embed.set_image(url=image_url)

                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Dog(bot))
