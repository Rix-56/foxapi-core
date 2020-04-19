from discord.ext import commands


class Commandes_utiles(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.command(description="La version du bot")
    async def ver(self, ctx):
        await ctx.send(
            '**Rixybot v1 Square release** lien pour inviter le bot : https://discordapp.com/api/oauth2/authorize?client_id=700046053029838878&permissions=8&scope=bot')

    @commands.command(description="La présentation du bot")
    async def presentation(self, ctx):
        await ctx.send(
            "Bonjour ! Je suis RixyBot , un bot créé en python.py et fait avec amouuurrr ! UwU ! Mon prefix : > ,Rix56 dit merci à ՇՎρԵ de l'avoir aider à faire une refonte générale de ce Bot pour le rendre compatible avec des commandes.")

def setup(client):
    client.add_cog(Commandes_utiles(client))
