import discord
from discord.ext import commands
import openai
import os

class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @commands.command(name="chat")
    async def chat(self, ctx, *, message):
        """Chat with ChatGPT!"""
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages=[{"role": "user", "content": message}],
                temperature=0.7,
                max_tokens=150
            )
            reply = response.choices[0].message.content
            await ctx.send(reply)
        except Exception as e:
            await ctx.send("Error talking to ChatGPT.")
            print(e)

async def setup(bot):
    await bot.add_cog(ChatGPT(bot))
