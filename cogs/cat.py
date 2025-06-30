from discord.ext import commands
import discord
import aiohttp

class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
                if resp.status != 200:
                    await ctx.send("Could not find cat :(")
                    return

                data = await resp.json()
                image_url = data[0]["url"]

                embed = discord.Embed(
                    title="Random Cat!",
                    description=":3",
                    color=discord.Color.green()
                )
                embed.set_image(url=image_url)

                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Cat(bot))
