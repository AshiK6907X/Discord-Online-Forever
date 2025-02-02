import discord
from discord.ext import tasks

TOKEN = "YOUR_DISCORD_TOKEN"

client = discord.Client(status=discord.Status.online, intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(
        activity=discord.Game(name="🔥 Always Online!"),
        status=discord.Status.online
    )


