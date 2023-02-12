import discord
from tictactoe import *
from rps import *
from hangman import *
from myakinator import *

async def loadGames(ctx, bot):
    embed = discord.Embed(
        title = "Please choose a game!",
        description = "1. Tic-Tac-Toe\n2. Rock-Paper-Scissors\n3. Hangman\n4. Akinator"
    )
    await ctx.channel.purge(limit=1)
    msg = await ctx.send(embed=embed)
    
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')
    await msg.add_reaction('3️⃣')
    await msg.add_reaction('4️⃣')
    
    def checkReaction(reaction, user):
        return user != bot.user and (str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣' or str(reaction.emoji) == '3️⃣' or str(reaction.emoji) == '4️⃣')
    
    reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkReaction)
    if str(reaction.emoji) == '1️⃣':
        await ticTacToe(ctx, bot)
    elif str(reaction.emoji) == '2️⃣':
        await rps(ctx, bot)
    elif str(reaction.emoji) == '3️⃣':
        await hangman(ctx, bot)
    elif str(reaction.emoji) == '4️⃣':
        await myakinator(ctx, bot)