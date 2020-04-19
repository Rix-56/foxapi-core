#on fait les imports des modules
import logging
import os
import mkdir

import discord
from discord.ext import commands

print("RixyBot - 0.1 Indev")
print("Connexion en cours à Discord...")

#on créer des logs

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='../rixybot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def get_prefix(client, message):
    # ici ce peut être une liste de prefix

    prefixes = ['>', '~']

    # on déternine et on change de prefix pour les message privé
    if not message.guild:
        prefixes = ['>>', '~~']

    # On returne les prefix

    return commands.when_mentioned_or(*prefixes)(client, message)

client = commands.Bot(
    # Creation du bot
    command_prefix=get_prefix,
    description='lol',
    owner_id='475215232961085440',
    case_insensitive=True
)

admin = [475215232961085440, 296028798527209472, 443804115991134228, 270903423371575296]

#on enlève la commande help
client.remove_command('help')

#on créer des events

@client.event
async def on_ready():
    print(f'Connecté à Discord : depuis votre token , je suis connecté en tant que {client.user.name} - {client.user.id}.')
    game = discord.Game("RixyBot v1 Square release - Tapez >help pour les commandes - Je pense que le Covid-19 est dû à un Pokémon sorti de laboratoire.")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_command_error(ctx, error):
    print(str(error))
    if "is not found" in str(error):
        await ctx.send('MDR ta cru que cette commande existait ? Petite astuce : met >help pour les commandes ;)')

#on créer des commandes

def starter():
    mkdir.mkdir("./cogs")
    for filename in os.listdir('./cogs'):
        # on vérifie que le fichier est bien l'extension python
        if filename.endswith('.py'):
            cog = filename[:-3]
            try:
                print(f'Chargement du cog : \n {cog}')
                client.load_extension(f'cogs.{cog}')
            except:
                print(f'Rechargement du cog : \n {cog}')
                client.unload_extension(f'cogs.{filename[:-3]}')
                client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def module(ctx, mode=None, extension = None):
    if mode == "load":
        if ctx.message.author.id in admin:
            if extension is None:
                await ctx.send("Vous n'avez pas demandé de module")
            try:
                client.load_extension(f'cogs.{extension}')
                await ctx.send("Le module a été chargé.")
            except:
                await ctx.send("Le module n'a pas été chargé")

        else:
            await ctx.send("Vous n'avez pas les droits d'administration.")

    elif mode == "unload":
        if ctx.message.author.id in admin:
            if extension is None:
                await ctx.send("Vous n'avez pas demandé de module")
            try:
                client.unload_extension(f'cogs.{extension}')
                await ctx.send("Le module a été déchargé.")
            except:
                await ctx.send("Le module n'a pas été déchargé")
        else:
            await ctx.send("Vous n'avez pas les droits d'administration.")


    elif mode == "reload":
        if ctx.message.author.id in admin:
            if extension is None:
                await ctx.send("Vous n'avez pas demandé de module")
            try:
                client.unload_extension(f'cogs.{extension}')
                client.load_extension(f'cogs.{extension}')
                await ctx.send("Le module a été rechargé.")
            except:
                await ctx.send("Le module n'a pas été rechargé")
        else:
            await ctx.send("Vous n'avez pas les droits d'administration.")

    elif mode is None:
        await ctx.send("Vous n'avez pas demandé une option pour la commande module.")

starter()

client.run("votre token ici", bot=True, reconnect=True)
