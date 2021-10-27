import os
os.system('pip install googletrans==3.1.0a0')
from discord.ext import commands
from googletrans import Translator


class Tr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['tran', 't'])
    async def translate(self, ctx, *, arg):
        translator = Translator()
        result = translator.translate(arg, dest='my')
        txt = f'{arg} ->\n{result.text}'
        await ctx.send(txt)
