import discord
from discord.ext import *
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #ładowanie tokenu bota

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '$', intents=intents)

@client.event #jak sie bot wlacza
async def on_ready():
    print("akadembot gotowy B)")
    await client.change_presence(activity=discord.Game(name="komendy: $komendy"))

@client.event #licznie członków po dołączeniu
async def on_member_join(member):
    channel = client.get_channel(820634014662131773)
    with open("/opt/akadembot/members.txt", 'r') as f:
        number = int(f.read()) + 1
    with open("/opt/akadembot/members.txt", 'w') as f:
        f.truncate()
        f.write(str(number))
    await channel.send(f"{member} jest {number} użytkownikiem")

@client.command() #dostepne komendy
async def komendy(ctx):
    embed=discord.Embed(title="Komendy", color=0x1a667f)
    embed.add_field(name="$members", value="wyświetla liczbę użytkowników", inline=False)
    embed.add_field(name="$members [ilość]", value="zmienia ilość użytkowników (admin only)", inline=False)
    await ctx.send(embed=embed)

@client.command() #komenda do zmieniania/wyswietlania liczby czlonkow
async def members(ctx, *, message = None):
    role = discord.utils.get(ctx.guild.roles, name="admini")
    if message == None:
        with open("/opt/akadembot/members.txt", 'r') as f:
            number = f.read()
            string = f"Obecnie na serwerze jest: {number} osób"
            await ctx.send(string)
    else:
        if role in ctx.author.roles:
            try:
                number = int(message)
            except:
                await ctx.send("Musisz wpisać liczbę")
            number = str(number)
            with open("/opt/akadembot/members.txt", 'w') as f:
                await ctx.send(f"Zmieniam liczbę użytkowników na: {number}")
                f.truncate()
                f.write(number)
            await ctx.send("Zmieniono")
        else:
            await ctx.send("Nie masz uprawnień aby to zrobić")


client.run(TOKEN)
