import discord
import datetime
from datetime import datetime
from discord.ext import commands
from config import *
from games import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX,
                   description="Game Bot for Python Project", intents=intents)


@bot.event
async def on_ready():
    print("I am Alive!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello, I am GameBot!")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.message.author}!")


@bot.command()
async def clear(ctx, amount: str):
    if amount == "all":
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=int(amount) + 1)


@bot.event
async def on_raw_reaction_add(payload):
    ourMessageID = 1073667604448808972
    if ourMessageID == payload.message_id:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name
        if emoji == '🟦':
            role = discord.utils.get(guild.roles, name="Blue")
        elif emoji == '🟥':
            role = discord.utils.get(guild.roles, name="Red")
        elif emoji == '🎮':
            role = discord.utils.get(guild.roles, name="Games")
        await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    ourMessageID = 1073667604448808972

    if ourMessageID == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name

        if emoji == '🟦':
            role = discord.utils.get(guild.roles, name="Blue")
        elif emoji == '🟥':
            role = discord.utils.get(guild.roles, name="Red")
        elif emoji == '🎮':
            role = discord.utils.get(guild.roles, name="Games")

        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("Member not found!")


@bot.command()
async def teams(ctx):
    embed = discord.Embed(
        title="Choose your role!",
        timestamp=datetime.now(),
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🟦')
    await msg.add_reaction('🟥')
    await msg.add_reaction('🎮')


@bot.command()
@commands.has_role("Games")
async def games(ctx):
    await loadGames(ctx, bot)

bot.run(TOKEN, reconnect=True)
