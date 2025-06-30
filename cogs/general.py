from discord.ext import commands
import discord
import os

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello")
        
    @commands.command(name="cogs")
    async def list_cogs(self, ctx):
        if not self.bot.cogs:
            await ctx.send("No cogs currently loaded.")
            
        cog_names = list(self.bot.cogs.keys())
        embed = discord.Embed(title="Loaded Cogs", description="\n".join(cog_names), color = discord.Color.green())
        await ctx.send(embed=embed)
        
    @commands.command(name="reload")
    @commands.is_owner()
    async def reload_cog(self, ctx, cog_name: str):
        """Reloads a specific cog"""
        try:
            await self.bot.reload_extension(f"cogs.{cog_name}")
            await ctx.send(f"Reloaded cog: {cog_name}")
        except Exception as e:
            await ctx.send(f"Failed to reload {cog_name}: {e}")

    @commands.command(name="reloadall")
    @commands.is_owner()
    async def reload_all_cogs(self, ctx):
        """Reloads all cogs in the cogs folder"""
        failed = []
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                cog = f"cogs.{filename[:-3]}"
                try:
                    await self.bot.reload_extension(cog)
                except Exception as e:
                    failed.append((cog, str(e)))
        if failed:
            msg = "\n".join([f"{c}: {err}" for c, err in failed])
            await ctx.send(f"Some cogs failed to reload:\n{msg}")
        else:
            await ctx.send("All cogs reloaded successfully!")

async def setup(bot):
    await bot.add_cog(General(bot))
