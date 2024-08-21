import discord
import os
from discord.ext import commands
from discord import app_commands
from api import config
from kad import name

#import subprocess
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all(), help_command=None, test_guilds=config.config['GUILD_ID'])# айди вашего сервера в квадратные скобки
a = ''


@bot.event
async def on_ready():
    await bot.tree.sync()
@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0xe51c1c,
    title='`Вот мои команды: \n!help - список команд\n' )
    await ctx.send(embed=embed)


@bot.tree.command(name="discr")
@app_commands.describe(
    discr='много букв',
)
async def add(interaction: discord.Interaction, discr: str):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{discr}')

    #print(a)
    # libr = {
    #     'Description': f'{discr}',
    # }
    # a = libr['Description']
    cahe = discr
    name(cahe)
    #os.startfile(r'C:\Users\flitme\Desktop\yolov20\kad_test\kad.py')
    #subprocess.Popen(r'C:\Users\flitme\Desktop\yolov20\kadinsky\kad.py', shell=True)
    print(a)

    channel = bot.get_channel(1031102919598161924)
    await channel.send(file=discord.File('copy.jpg'))
    os.remove("copy.jpg")

bot.run(config.config['TOKEN'])