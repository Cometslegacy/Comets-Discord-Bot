import random
import re
from discord.ext import commands

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["roll", "r"])
    async def dice(self, ctx, *, roll: str):
        """
        Rolls dice using standard notation. Examples:
        1d6 - Roll one six-sided die
        2d20+5 - Roll two 20-sided dice and add 5
        4d8-2 - Roll four 8-sided dice and subtract 2
        """
        match = re.fullmatch(r'(\d*)d(\d+)([+-]\d+)?', roll.replace(" ", ""))
        if not match:
            await ctx.send("Invalid format. Use NdM±X format like 2d6, 1d20+4, etc.")
            return

        num_dice = int(match.group(1)) if match.group(1) else 1
        die_size = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0

        if num_dice <= 0 or die_size <= 0 or num_dice > 100:
            await ctx.send("Invalid dice amount or die size. Try something reasonable.")
            return

        rolls = [random.randint(1, die_size) for _ in range(num_dice)]
        total = sum(rolls) + modifier

        roll_str = " + ".join(str(r) for r in rolls)
        if modifier:
            sign = "+" if modifier > 0 else "-"
            roll_str += f" {sign} {abs(modifier)}"

        #await ctx.send(f"You rolled: {roll_str} = **{total}**")
        await ctx.send(f"You rolled: {rolls} {modifier} = **{total}**")

async def setup(bot):
    await bot.add_cog(Dice(bot))
