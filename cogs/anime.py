import discord
from discord.ext import commands
import aiohttp

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="anime")
    async def anime(self, ctx, *, tags="rating:safe 1girl score:>100"):
        """Get a random Danbooru image with optional tags. Default: safe rating."""

        query_tags = '+'.join(tags.split())  # Convert tags to Danbooru format
        query_tags += "+rating:safe+score:>100"
        url = f"https://danbooru.donmai.us/posts.json?tags={query_tags}&limit=1&random=true"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    await ctx.send("Failed to fetch image from Danbooru.")
                    return

                data = await response.json()

                if not data:
                    await ctx.send("No results found with those tags.")
                    return

                post = data[0]  # First (and only) post from API

                image_url = post.get("file_url") or post.get("large_file_url") or post.get("preview_file_url")
                if not image_url:
                    await ctx.send("Could not retrieve image URL.")
                    return

                await ctx.send(image_url)

async def setup(bot):
    await bot.add_cog(Anime(bot))
