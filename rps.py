import discord
import random
from discord.ext import commands


async def rps(ctx, bot):
    msg = await ctx.send("Choose rock, paper or scissors!")
    await msg.add_reaction('🪨')
    await msg.add_reaction('📜')
    await msg.add_reaction('✂️')
    items = ['🪨', '📜', '✂️']
    computer = random.choice(items)

    def checkNotBot(reaction, user):
        return user != bot.user

    reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkNotBot)
    player = str(reaction.emoji)
    if player == computer:
        embed = discord.Embed(
            title="Tie!",
            description=f"We both chose {player}!"
        )
        await ctx.send(embed=embed)
    elif player == '🪨':
        if computer == '📜':
            embed = discord.Embed(
                title="You Lose!",
                description=f"I picked: {computer}\n\nYou picked: {player}\n\n{computer} covers {player}!"
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="You win!",
                description=f"I picked: {computer}\n\nYou picked: {player}\n\n{player} crushes {computer}!"
            )
            await ctx.send(embed=embed)
    elif player == '📜':
        if computer == '✂️':
            embed = discord.Embed(
                title="You lose!",
                description=f"I picked: {computer}\n\nYou picked: {player}\n\n{computer} cuts {player}!"
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="You win!",
                description=f"I picked: {computer}\n\nYou picked: {player}\n\n{player} covers {computer}!"
            )
            await ctx.send(embed=embed)
    elif player == '✂️':
        if computer == '🪨':
            embed = discord.Embed(
                title="You lose!",
                description=f"I picked: {computer}\n\nYou picked: {player}\n\n{computer} smashes {player}!"
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="You win!",
                description=f"I picked: {computer}\n\nYou picked: {player}\n\n{player} cuts {computer}!"
            )
            await ctx.send(embed=embed)

    msg = await ctx.send("Do you want to play again?")
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')
    reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkNotBot)
    if str(reaction.emoji) == '✅':
        await ctx.channel.purge(limit=3)
        await rps(ctx, bot)
    else:
        await ctx.channel.purge(limit=3)
        await ctx.send("Thank you for playing Rock-Paper-Scissors!")
