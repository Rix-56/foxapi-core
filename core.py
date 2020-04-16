#on fait les imports des modules
import asyncio
import logging

import discord
from discord.ext import commands

print("RixyBot - 0.1 Indev")
print("Connexion en cours à Discord...")

#créer des logs

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='rixybot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#on set un prefix

client = commands.Bot(command_prefix=">")

#on enlève la commande help

client.remove_command('help')

#on créer des events

@client.event
async def on_ready():
    print('Connecté à Discord : depuis votre token , je suis connecté en tant que {0.user}.'.format(client))
    game = discord.Game("RixyBot v0 Indev - tapez >help pour les commandes")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_error(error, ctx):
    if error == "":
        return ctx.send("MDR commande incorrecte")
#on créer des commandes
@client.command()
async def help(ctx):
    await ctx.send('Pour le module utile , tapez >modulehelp util.Pour les autres , tapez modulehelp other.')

@client.command()
async def ver(ctx):
    await ctx.send('**Rixybot v0 (indev)** lien pour inviter le bot : https://discordapp.com/api/oauth2/authorize?client_id=700046053029838878&permissions=8&scope=bot')

@client.command()
async def how_2_build_a_bot_with_python_py(ctx):
    await ctx.send('Oh , alors comme ça on veut faire un **bot** en **python.py ?** Alors je te conseille ce **lien :** https://discordpy.readthedocs.io/en/latest/intro.html (par contre le guide est en anglais)')

@client.command()
async def modulehelp(ctx, *,args = None):
    if args == "util":
        await ctx.send('Commandes du module utile : ver, presentation.')
    if args == "other":
        await ctx.send('Commandes du module other : how_2_build_a_bot_with_python_py, jsp_si_je_tadore, repete')

@client.command()
async def presentation(ctx):
    await ctx.send("Bonjour ! Je suis RixyBot , un bot créé en python.py et fait avec amouuurrr ! UwU ! Mon prefix : > ,Rix56 dit merci à ՇՎρԵ de l'avoir aider à faire une refonte générale de ce Bot pour le rendre compatible avec des commandes.")

@client.command()
async def jsp_si_je_tadore(ctx):
    await ctx.send('Allez , si tu adores moi , le bot , met la réaction 👍 (ou si tu est pas ton bot préféré alors attends que je réponde.)')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '👍'
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('👎 oh ben je suis décu...')
    else:
        await ctx.send('👍 ha un nouveau pote !')

@client.command()
async def pile_ou_face(ctx):
    await ctx.send('Under construction !')

@client.command()
async def repete(ctx, arg):
    await ctx.send(arg)

client.run("Votre token")
