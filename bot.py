import asyncio

import discord
import logging
print("RixyBot - 0.1 Indev")
print("Connexion en cours à discord...")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='rixybot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

rixybot = discord.Client()

@rixybot.event
async def on_ready():
    print('Depuis votre token , je suis connecté en tant que {0.user}.'.format(rixybot))
    game = discord.Game("Mdrrr tu croyais que j'allais mettre >help ??? T'es trop drôle xD")
    await rixybot.change_presence(status=discord.Status.idle, activity=game, afk=True)

@rixybot.event
async def on_message(message):
    if message.author == rixybot.user:
        return

    if message.content.startswith('>help'):
        await message.channel.send('Pour le module utile , tapez >modulehelp util.Pour les autres , tapez >modulehelp other.')

    if message.content.startswith('>ver'):
        await message.channel.send('**Rixybot v0 (indev)** lien pour inviter le bot : https://discordapp.com/api/oauth2/authorize?client_id=700046053029838878&permissions=8&scope=bot')

    if message.content.startswith('>how-2-build-a-bot-with-python.py'):
        await message.channel.send('Oh , alors comme ça on veut faire un **bot** en **python.py ?** Alors je te conseille ce **lien :** https://discordpy.readthedocs.io/en/latest/intro.html (par contre le guide est en anglais)')

    if message.content.startswith('>modulehelp util'):
        await message.channel.send('Commandes du module utile : ver, presentation.')

    if message.content.startswith('>modulehelp other'):
        await message.channel.send('Commandes du module other : how-2-build-a-bot-with-python.py, jsp-si-je-tadore')

    if message.content.startswith('>presentation'):
        await message.channel.send('Bonjour ! Je suis RixyBot , un bot créé en python.py et fait avec amouuurrr ! UwU ! Mon prefix : >')

    if message.content.startswith('>jsp-si-je-tadore'):
        channel = message.channel
        await channel.send('Allez , si tu adores moi , le bot , met la réaction 👍 (ou si tu est pas ton bot préféré alors attends que je réponde.)')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await rixybot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎 oh ben je suis décu...')
        else:
            await channel.send('👍 ha un nouveau pote !')

    if message.content.startswith('>pile-ou-face'):
        await message.channel.send("Under construction !")

rixybot.run("NzAwMDQ2MDUzMDI5ODM4ODc4.Xpg0LA.p7ckf61rQZL6h4j-fpPgeB-6bYk")