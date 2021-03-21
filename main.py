import discord
from discord.ext import *
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = '$')
@client.event #when bot is turned on
async def on_ready():
    print("akadembot gotowy B)")
    await client.change_presence(activity=discord.Game(name="komendy: $komendy"))
client.run(TOKEN)
