from discord.ext import commands
import discord


class Autres_commandes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="Le bot répète ce que vous dites")
    async def repete(self, ctx, *, arg1):
        repete_embed = discord.Embed(title="Répété", color=0x3498DB)
        repete_embed.set_footer(text=f'En réponse à {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        repete_embed.add_field(name="Texte :", value=arg1, inline=False)
        await ctx.send(embed=repete_embed)

    @commands.command(description="Comment créer un bot avec Discord.py")
    async def how_2_build_a_bot_with_discord_py(self, ctx):
        embed = discord.Embed(title="Comment créer un bot en discord.py", color=0x11806A)
        embed.set_footer(text=f'En réponse à {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Voici ce que je te dit :", value="Oh , alors comme ça on veut faire un **bot** en **Discord.py ?** Alors je te conseille ce **lien :** https://discordpy.readthedocs.io/en/latest/api.html (par contre le guide est en anglais)",inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Autres_commandes(client))
