import json
import discord
from discord.ext import commands


def pfx(ctx):
    with open('prefixes.json', 'r') as f:
        pfxes = json.load(f)
    return pfxes[str(ctx.guild.id)]


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['h'], case_insensitive=True, invoke_without_command=True)
    async def help(self, ctx):
        hp = f'The prefix is `{pfx(ctx)}`\nYou can change it with `{pfx(ctx)}setprefix <new prefix>`\n' \
             f'Use `{pfx(ctx)}help <command>` for more info on a specific command!'
        em = discord.Embed(title='Commands List', colour=discord.Colour.blurple(), description=hp)
        music = '`join`, `leave`, `play`, `pause`, `resume`, `skip`, ' \
            '`forceskip`, `queue`, `remove`, `clearqueue`, `nowplaying`'
        unizawgyi = '`unicode`, `zawgyi`'
        em.add_field(inline=False, name=':notes: Music Player', value=music)
        em.add_field(inline=False, name=':notepad_spiral: Zawgyi/Unicode', value=unizawgyi)
        await ctx.send(embed=em)

    @help.command(aliases=['j', 'connect'])
    async def join(self, ctx):
        d = f'If you are **in a voice channel** and use this command, ' \
            f'I\'ll join **the same voice channel** with you\n\n'\
            f'You can also directly call with `play` command without using `join`\n\n**Aliases:** `j`, `connect`'
        em = discord.Embed(title='Help `join` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['dc', 'dis', 'disconnect', 'bye'])
    async def leave(self, ctx):
        d = f'When I\'m in **the same voice channel** with you, I\'ll **disconnect** from that voice channel\n\n' \
            f'Note that all the queue(playlist) will be reset\n\n**Aliases:** `disconnect`, `dc`, `dis`, `bye`'
        em = discord.Embed(title='Help `leave` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['p'])
    async def play(self, ctx):
        d = f'Syntax: `{pfx(ctx)}play <youtubelink or song name>`\n\nI\'ll **play the song** you enter\n' \
            f'If I\'m currently playing a song, ' \
            f'this command will **add the song to the queue**\n\n**Aliases:** `p`'
        em = discord.Embed(title='Help `play` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['stop'])
    async def pause(self, ctx):
        d = f'I\'ll **pause currently playing song**\nYou can resume with `resume` command\n\n' \
            f'**Aliases:** `stop`'
        em = discord.Embed(title='Help `pause` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command()
    async def resume(self, ctx):
        d = f'You can **resume the paused song** with this command\n\n'
        em = discord.Embed(title='Help `resume` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliased=['s'])
    async def skip(self, ctx):
        d = f'I\'ll **skip** to the next song from the queue\n' \
            f'**80% of the voice channel must vote to skip for it to pass.**\n\n' \
            f'**Aliases:** `s`'
        em = discord.Embed(title='Help `skip` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['fs'])
    async def forceskip(self, ctx):
        d = f'You must have `Manage Channels` permission to use this command\n' \
            f'I\'ll **skip** the current song **without voting.**\n\n' \
            f'**Aliases:** `fs`'
        em = discord.Embed(title='Help `forceskip` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['q'])
    async def queue(self, ctx):
        d = f'I\'ll show you the **current queued list**\n\n' \
            f'**Aliases:** `q`'
        em = discord.Embed(title='Help `queue` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command()
    async def remove(self, ctx):
        d = f'Syntax: `{pfx(ctx)}remove <index>`\n\nYou can **remove the queued song** with this command\n' \
            f'You can check the `<index>` with `queue` command'
        em = discord.Embed(title='Help `remove` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['clrq'])
    async def clearqueue(self, ctx):
        d = f'You must have `Manage Channels` permission to use this command\n' \
            f'You can **clear the whole queue** with this command\n\n' \
            f'**Aliases:** `clrq`'
        em = discord.Embed(title='Help `clearqueue` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['np'])
    async def nowplaying(self, ctx):
        d = f'I\'ll show you the **current playing song**\n\n' \
            f'**Aliases:** `np`'
        em = discord.Embed(title='Help `nowplaying` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['u'])
    async def unicode(self, ctx):
        d = f'I\'ll change your Myanmar **Unicode text to Zawgyi**\n\n' \
            f'**Aliases:** `u`'
        em = discord.Embed(title='Help `unicode` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)

    @help.command(aliases=['z'])
    async def zawgyi(self, ctx):
        d = f'I\'ll change your Myanmar **Zawgyi text to Unicode**\n\n' \
            f'**Aliases:** `z`'
        em = discord.Embed(title='Help `zawgyi` command', colour=discord.Colour.random(), description=d)
        await ctx.send(embed=em)
