from discord.ext import commands
import discord


class Commandes_utiles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="La version du bot")
    async def ver(self, ctx):
        ver_embed = discord.Embed(title="Fox API version information", color=0xE67E22)
        ver_embed.set_footer(text=f'En réponse à {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        ver_embed.add_field(name="Version :",
                            value="**Fox API v3BETA Embed release** lien pour inviter le bot : https://discordapp.com/api/oauth2/authorize?client_id=700046053029838878&permissions=8&scope=bot",
                            inline=False)
        await ctx.send(embed=ver_embed)

    @commands.command(description="La présentation du bot")
    async def presentation(self, ctx):
        pre_embed = discord.Embed(title="La présentation de Fox API", color=0xE74C3C)
        pre_embed.set_footer(text=f'En réponse à {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        pre_embed.add_field(name="Présentation :",
                            value="Bonjour ! Je suis FoxAPI , un bot créé en python.py et fait avec amouuurrr ! UwU !\nMon prefix : >\nRix56 dit merci à ՇՎρԵ de l'avoir aider à faire une refonte générale de ce Bot pour le rendre compatible avec des commandes.",
                            inline=False)
        await ctx.send(embed=pre_embed)

    @commands.command(description="Le changelog")
    async def changelog(self, ctx):
        ch_embed = discord.Embed(title="Changelog de Fox API", color=0x95A5A6)
        ch_embed.set_footer(text=f'En réponse à {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        ch_embed.add_field(name="Le changelog :", value="Changelog V2 (Embed release):\n-Recréation de toutes les commandes en embed\n-Ajout de la commande changelog" ,inline=False)
        await ctx.send(embed=ch_embed)

def setup(client):
    client.add_cog(Commandes_utiles(client))
