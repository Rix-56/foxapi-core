from discord.ext import commands
from jedit import *
import time
import datetime
import bot
import random
import tracemalloc
import asyncio

tracemalloc.start()


class Rank(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.command(description="Ton rank")
    async def rank(self, ctx):
        UserId = str(ctx.message.author.id)

        coins = reader("/home/rix56/pycharm/BOT/jsondata/rank.json")
        animals = reader("/home/rix56/pycharm/BOT/jsondata/animals.json")
        listeKeys = list(coins.keys())
        listeKeys2 = list(animals.keys())
        if UserId not in listeKeys:
            print('Created profile')
            coins[UserId] = 0
        if UserId not in listeKeys2:
            print('Created profile')
            animals[UserId] = 0

        print(f"Id :{ctx.message.author.id}\n{coins[UserId]} €\n{animals[UserId]} animals")

        with open("/home/rix56/pycharm/BOT/jsondata/rank.json", 'w', encoding='utf8') as jsonFile:
            json.dump(coins, jsonFile, indent=4)

        with open("/home/rix56/pycharm/BOT/jsondata/animals.json", 'w', encoding='utf8') as jsonFile:
            json.dump(animals, jsonFile, indent=4)

        if animals[UserId] == 1 or animals[UserId] == 0:
            await ctx.send(f"Vous avez {coins[UserId]} € et {animals[UserId]} animal.")
        else:
            await ctx.send(f"Vous avez {coins[UserId]} € et {animals[UserId]} animaux.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == bot.client.user:
            return

        message_random = random.randint(1, 500)

        if message_random == 2:
            global money
            money = random.randint(1, 50)
            try:
                await message.channel.send(f"{money} € en giveaway sont mis en jeu ! Mettez >money_recup pour les avoir !")
            except asyncio.TimeoutError:
                await message.channel.send("Trop tard !")
                money = 0

    @commands.command(description="Quand il y a un giveaway , on peut utiliser cette commande !")
    async def money_recup(self, ctx):
        try:
            if money >> 0:
                UserId = str(ctx.message.author.id)
                coins = reader("/home/rix56/pycharm/BOT/jsondata/rank.json")
                listeKeys = list(coins.keys())
                if UserId not in listeKeys:
                    print('Created profile')
                    coins[UserId] = 0
                coins[UserId] += money
                with open("/home/rix56/pycharm/BOT/jsondata/rank.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(coins, jsonFile, indent=4)
                await ctx.send(f"{ctx.message.author.name} a gagné {money} € !")
        except:
            await ctx.send(f"Il n'y a pas actuellement d'argent mis en jeu , {ctx.message.author.name}.")

    @commands.command(description="Payer un animal")
    async def pay_animal(self, ctx):
        UserId = str(ctx.message.author.id)
        coins = reader("/home/rix56/pycharm/BOT/jsondata/rank.json")
        animals = reader("/home/rix56/pycharm/BOT/jsondata/animals.json")
        listeKeys = list(coins.keys())
        listeKeys2 = list(animals.keys())
        if UserId not in listeKeys:
            await ctx.send("Vous n'avez pas de compte utilisateur.Faites >rank et il sera automatiquement créé !")
        if UserId not in listeKeys2:
            await ctx.send("Vous n'avez pas de compte utilisateur.Faites >rank et il sera automatiquement créé !")
        else:
            if coins[UserId] >= 20:
                coins[UserId] -= 20
                animals[UserId] += 1
                with open("/home/rix56/pycharm/BOT/jsondata/rank.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(coins, jsonFile, indent=4)
                with open("/home/rix56/pycharm/BOT/jsondata/animals.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(animals, jsonFile, indent=4)
                await ctx.send("Vous avez payé un animal !")
            else:
                await ctx.send("Vous n'avez pas assez d'argent !")


def setup(client):
    client.add_cog(Rank(client))
