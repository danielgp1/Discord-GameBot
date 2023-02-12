import akinator
import discord
from akinator.async_aki import Akinator
from akinator.exceptions import CantGoBackAnyFurther, InvalidAnswerError


async def myakinator(ctx, bot):
    embed = discord.Embed(
        title="Akinator is here to guess!",
        description="\nChoose 👍 if the answer is \'Yes\'\n\n \
        Choose 👎 if the answer is \'No\'\n\nChoose ❔ if you are not sure\n\n \
        Choose ◀️ to go back to the previous question\n\nChoose 🛑 to end the game\n"
    )
    await ctx.send(embed=embed)

    def checkNotBot(reaction, user):
        return user != bot.user
    try:
        aki = akinator.async_aki.Akinator()
        q = await aki.start_game()
        firstBack = False
        while aki.progression <= 80:
            if firstBack == True:
                await ctx.channel.purge(limit=1)
            firstBack = False
            msg = await ctx.send(q)
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')
            await msg.add_reaction('❔')
            await msg.add_reaction('◀️')
            await msg.add_reaction('🛑')

            reaction, user = await bot.wait_for("reaction_add", timeout=60.0, check=checkNotBot)

            if str(reaction.emoji) == '👍':
                q = await aki.answer('y')
            elif str(reaction.emoji) == '👎':
                q = await aki.answer('n')
            elif str(reaction.emoji) == '❔':
                q = await aki.answer('p')
            elif str(reaction.emoji) == '◀️':
                try:
                    q = await aki.back()
                except:
                    await ctx.channel.purge(limit=1)
                    await ctx.send("No previous questions!")
                    firstBack = True
                    continue
            elif str(reaction.emoji) == '🛑':
                await ctx.channel.purge(limit=2)
                await ctx.send("The game of Akinator has been ended!")
                return
            await ctx.channel.purge(limit=1)

        await aki.win()
        msg = await ctx.send(f"It's {aki.first_guess['name']}!\nWas I correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')
        reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkNotBot)
        if str(reaction.emoji) == '✅':
            await ctx.send("I knew it!")
        else:
            await ctx.send("Kinda sad, ngl")
        msg = await ctx.send(f"Do you want to play again?")
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')
        reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkNotBot)
        if str(reaction.emoji) == '✅':
            await ctx.channel.purge(limit=4)
            await myakinator(ctx, bot)
        else:
            await ctx.channel.purge(limit=4)
            await ctx.send("Thank you for playing Akinator!")
    except Exception as e:
        await ctx.send(e)
