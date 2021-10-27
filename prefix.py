import json
import discord
from discord.ext import commands


class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = '.'
        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes.pop(str(guild.id))
        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.command(aliases=['changeprefix', 'prefixchange', 'prefixset'])
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix
        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        em = discord.Embed(colour=discord.Colour.random(), description=f'**Now, the prefix is `{prefix}`**')
        em.set_author(icon_url=ctx.author.avatar_url, name='Changed command prefix')
        em.set_footer(text='Thanks for using me UwU')
        await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user in message.mentions:
            with open('prefixes.json', 'r') as f:
                prefix = json.load(f)
            em = discord.Embed(description=f'**Command Prefix is `{prefix[str(message.guild.id)]}`**',
                               colour=discord.Colour.random())
            await message.channel.send(embed=em)
