import discord
from discord.ext import commands
import os

class Moderation(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    #Kick Command------------------------------------------------------
    @commands.command(name = "kick")
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)    
        await ctx.send(f'Kicked {member.mention}. Reason: {reason}')

    #Ban Command------------------------------------------------------
    @commands.command(name = "ban")
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)  
        await ctx.send(f'Banned {member.mention}. Reason: {reason}')

    #Unban Command-----------------------------------------------------
    @commands.command(name = "unban")
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.banned_users

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

    #Delete Messages (AKA Purge "X", default 5)------------------------
    @commands.command(aliases = ['purge', 'delete']) #we can still use the main command, !clear
    async def clear(self, ctx, amount=5,):
        await ctx.channel.purge(limit=amount)


"""   
    @commands.command(name='unban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user}")
"""

"""
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
"""

async def setup(bot):
    await bot.add_cog(Moderation(bot))