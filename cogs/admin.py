from discord.ext import commands
from jedit import *
import discord


class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Permet de avertir un membre")
    async def warn(self, ctx, user: discord.Member, *, raison=None):
        UserId = str(user.id)

        warns = reader("/home/rix56/pycharm/BOT/jsondata/warn.json")
        listeKeys = list(warns.keys())
        if UserId not in listeKeys:
            print('Warned user')
            warns[UserId] = 0

        warns[UserId] += 1

        if warns[UserId] >= 3:
            warns[UserId] = 0
            try:
                await user.kick()
            except:
                await ctx.send("Bot as ")
            await user.send("Vous avez été kick du serveur {}".format(ctx.guild.name))

        print(f"{warns[UserId]} \n {user.display_name}")

        with open("/home/rix56/pycharm/BOT/jsondata/warn.json", 'w', encoding='utf8') as jsonFile:
            json.dump(warns, jsonFile, indent=4)

        await user.send(f"Vous avez eu un avertissement ! Raison : {raison}")
        await ctx.send(f"Le membre {user.mention} a été averti sur {ctx.guild.name} pour la raison suivante : {raison}")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Connecté à Discord : depuis votre token , je suis connecté en tant que {self.client.user.name} - {self.client.user.id}.')
        print('Le tag discord : {0.user}.'.format(self.client))
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game("FoxAPI v3 JSON release - Tapez >help pour les commandes - Je pense que le Covid-19 est dû à un Pokémon sorti de laboratoire."))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(str(error))
        if "is not found" in str(error):
            await ctx.send('MDR ta cru que cette commande existait ? Petite astuce : met >help pour les commandes :wink:')


def setup(client):
    client.add_cog(admin(client))
