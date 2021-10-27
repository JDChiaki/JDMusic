# import discord
from discord.ext import commands


class Emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['e'])
    async def emoji(self, ctx, arg, count=1):
        if int(count) > 17:
            await ctx.send('**Are you trying to spam???? idiot!**')
            await ctx.send('https://thumbs.gfycat.com/CheapWaryBaboon-size_restricted.gif')
            return 
        emojis = [i for i in ctx.guild.emojis]
        emoji = None
        for i in emojis:
            if arg in i.name:
                emoji = i
                break
        if emoji is None:
            return
        t = ''
        for i in range(int(count)):
            t += f'<a:{emoji.name}:{emoji.id}>'
        await ctx.send(t)
