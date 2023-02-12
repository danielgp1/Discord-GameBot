import discord
import random
from words import *

HANGMAN0 = "-------"

HANGMAN1 = "  |\n" \
           "  |\n" \
           "  |\n" \
           "  |\n" \
           "  |"

HANGMAN2 = " -------\n" \
           " |\n" \
           " |\n" \
           " |\n" \
           " |\n" \
           " |"

HANGMAN3 = " -------\n" \
           " |/\n" \
           " |\n" \
           " |\n" \
           " |\n" \
           " |"

HANGMAN4 = " -------\n" \
           " |/----|\n" \
           " |\n" \
           " |\n" \
           " |\n" \
           " |"

HANGMAN5 = " -------\n" \
           " |/----|\n" \
           " |---- 0\n" \
           " |\n" \
           " |\n" \
           " |"

HANGMAN6 = " -------\n" \
           " |/----|\n" \
           " |---- O\n" \
           " |-----|\n" \
           " |\n" \
           " |"

HANGMAN7 = " -------\n" \
           " |/----|\n" \
           " |---- O\n" \
           " |----/|\n" \
           " |\n" \
           " |"

HANGMAN8 = " -------\n" \
           " |/----|\n" \
           " |---- O\n" \
           " |----/|\\ \n" \
           " |\n" \
           " |"

HANGMAN9 = " -------\n" \
           " |/----|\n" \
           " |---- O\n" \
           " |----/|\\ \n" \
           " |----/\n" \
           " |"

HANGMAN10 = " -------\n" \
            " |/----|\n" \
            " |---- O\n" \
            " |----/|\\ \n" \
            " |----/ \\ \n" \
            " |"

HANGMEN = [HANGMAN10, HANGMAN9, HANGMAN8, HANGMAN7, HANGMAN6, HANGMAN5, HANGMAN4, HANGMAN3, HANGMAN2, HANGMAN1,
           HANGMAN0]


async def hangman(ctx, bot):
    alphabet = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']
    emojis = {
        '🇦': 'a',
        '🇧': 'b',
        '🇨': 'c',
        '🇩': 'd',
        '🇪': 'e',
        '🇫': 'f',
        '🇬': 'g',
        '🇭': 'h',
        '🇮': 'i',
        '🇯': 'j',
        '🇰': 'k',
        '🇱': 'l',
        '🇲': 'm',
        '🇳': 'n',
        '🇴': 'o',
        '🇵':  'p',
        '🇶': 'q',
        '🇷': 'r',
        '🇸': 's',
        '🇹': 't',
        '🇺': 'u',
        '🇻': 'v',
        '🇼': 'w',
        '🇽': 'x',
        '🇾': 'y',
        '🇿': 'z'
    }
    lives = 10
    word = random.choice(WORDS)
    print(word)
    guess_word = ['?' for i in word]
    
    while("".join(guess_word).find('?') != -1):
        guess_word_str = " ".join(guess_word)
        embed = discord.Embed(
            title = "Your life is in your hands!",
            description = f"Tries left: {lives}\n\n" + HANGMEN[lives]
        )
        await ctx.send(embed=embed)
        await ctx.send(f"Current word: {guess_word_str}")
        if lives == 0:
            break
        await showLetters(ctx, alphabet)
            
        def checkNotBot(reaction, user):
            return user != bot.user
        
        reaction, user = await bot.wait_for("reaction_add", timeout=60.0, check=checkNotBot)
        
        guess = str(reaction.emoji)
        found = checkGuess(guess, word, guess_word, emojis, alphabet)
        lives = checkLives(lives, found)
        await ctx.channel.purge(limit=4)
        
    
    if(lives == 0):
        msg = await ctx.send(f"You died! The word was {word}! Do you want to play again?")
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')
        reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkNotBot)
        if str(reaction.emoji) == '✅':
            alphabet = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']
            await ctx.channel.purge(limit=3)
            await hangman(ctx, bot)
        else:
            await ctx.channel.purge(limit=3)
            await ctx.send("Thank you for playing Hangman!")
    else:
        msg = await ctx.send(f"You gussed it! Do you want to play again?")
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')
        reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=checkNotBot)
        if str(reaction.emoji) == '✅':
            alphabet = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']
            await ctx.channel.purge(limit=1)
            await hangman(ctx, bot)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send("Thank you for playing Hangman!")

        
async def showLetters(ctx, alphabet):
    msg1 = await ctx.send("Choose!")
    for i in range(int(len(alphabet) / 2)):
        await msg1.add_reaction(alphabet[i])
    msg2 = await ctx.send("A letter!")    
    for i in range(int(len(alphabet) / 2), len(alphabet)):
        await msg2.add_reaction(alphabet[i])
        
    
def checkGuess(guess, word, guess_word, emojis, alphabet):
    found = False
    letter = emojis[guess]
    alphabet.remove(guess)
    for i in range(len(word)):
        if word[i] == letter:
            found = True
            guess_word[i] = letter
    return found

def checkLives(lives, flag):
    if not flag:
        return lives - 1
    return lives