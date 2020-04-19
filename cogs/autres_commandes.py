from discord.ext import commands


class Autres_commandes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="Le bot répète ce que vous dites")
    async def repete(self, ctx, *, arg1):
        await ctx.send(arg1)

    @commands.command(description="Comment créer un bot avec Discord.py")
    async def how_2_build_a_bot_with_discord_py(self, ctx):
        await ctx.send('Oh , alors comme ça on veut faire un **bot** en **Discord.py ?** Alors je te conseille ce **lien :** https://discordpy.readthedocs.io/en/latest/intro.html (par contre le guide est en anglais)')


def setup(client):
    client.add_cog(Autres_commandes(client))
