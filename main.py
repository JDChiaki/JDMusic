import json
import os
import discord
from prefix import Prefix
from discord.ext import commands
from music import Player
from help import Help
from rabbit import Rabbit
from keep_alive import keep_alive
from emoji import Emoji
from tran import Tr

async def get_prefix(_, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    try:
        return prefixes[str(message.guild.id)]
    except KeyError:
        print('To leave: ' + str(message.guild.id) + str(message.guild.name))
        return '!!!'


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, help_command=None)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
@commands.is_owner()
async def leave_guild(ctx, guild: discord.Guild):
    await guild.leave()
    await bot.get_channel(879365987860893739).send(f'{ctx.author} commands!\nLeaved from **{guild.name}**: {guild.id}')

@bot.command(aliases=['gg'])
@commands.is_owner()
async def check_guilds(ctx):
    for guild in bot.guilds:
        t = f'{guild.id}: {guild.name}\n{guild.owner}\n{guild.member_count}'
        await ctx.send(t)

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Player(bot))
    bot.add_cog(Prefix(bot))
    bot.add_cog(Help(bot))
    bot.add_cog(Rabbit(bot))
    bot.add_cog(Emoji(bot))
    bot.add_cog(Tr(bot))

bot.loop.create_task(setup())
keep_alive()
bot.run(os.environ['TOKEN'])
