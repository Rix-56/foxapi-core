import discord
import random
from discord.ext import commands
import bot
import asyncio

colors = {
    'DEFAULT': 0x000000,
    'WHITE': 0xFFFFFF,
    'AQUA': 0x1ABC9C,
    'GREEN': 0x2ECC71,
    'BLUE': 0x3498DB,
    'PURPLE': 0x9B59B6,
    'LUMINOUS_VIVID_PINK': 0xE91E63,
    'GOLD': 0xF1C40F,
    'ORANGE': 0xE67E22,
    'RED': 0xE74C3C,
    'GREY': 0x95A5A6,
    'NAVY': 0x34495E,
    'DARK_AQUA': 0x11806A,
    'DARK_GREEN': 0x1F8B4C,
    'DARK_BLUE': 0x206694,
    'DARK_PURPLE': 0x71368A,
    'DARK_VIVID_PINK': 0xAD1457,
    'DARK_GOLD': 0xC27C0E,
    'DARK_ORANGE': 0xA84300,
    'DARK_RED': 0x992D22,
    'DARK_GREY': 0x979C9F,
    'DARKER_GREY': 0x7F8C8D,
    'LIGHT_GREY': 0xBCC0C0,
    'DARK_NAVY': 0x2C3E50,
    'BLURPLE': 0x7289DA,
    'GREYPLE': 0x99AAB5,
    'DARK_BUT_NOT_BLACK': 0x2C2F33,
    'NOT_QUITE_BLACK': 0x23272A
}

class Jeux(commands.Cog):

    # On initialise la classe

    def __init__(self, client):
        self.client = client

    @commands.command(description='Posez une question à votre Bot', aliases=['8ball', '8balls'])
    async def _8ball(self, ctx, *, question=None):
        responses = [" Essaye plus tard ",
                     " Essaye encore ",
                     " Pas d'avis ",
                     " C'est ton destin ",
                     " Le sort en est jeté ",
                     " Une chance sur deux ",
                     " Repose ta question ",
                     " D'après moi oui ",
                     " C'est certain ",
                     " Oui absolument ",
                     " Tu peux compter dessus ",
                     " Sans aucun doute ",
                     " Très probable ",
                     " Oui ",
                     " C'est bien parti ",
                     " C'est non ",
                     " Peu probable ",
                     " Faut pas rêver ",
                     " N'y compte pas ",
                     " Impossible ",
                     " Si tu continue à m'ennuyer je vais te faire du mal "
                     ]
        response_jeu = discord.Embed(title='Réponse à ta question', color=0x1ABC9C)

        response_jeu.set_footer(text=f'En réponse à {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        response_jeu.add_field(name='Question', value=ctx.message.content, inline=False)
        response_jeu.add_field(name="Réponse", value=random.choice(responses), inline=False)
        if question is None:
            await ctx.send("Veuillez poser une question.")
        if question is not None:
            await ctx.send(embed=response_jeu)

    @commands.command(description="Si tu ne sais pas si tu m'adores...")
    async def jsp_si_je_tadore(self, ctx):
        response_jeu = discord.Embed(title="Je sais pas si je t'adore", color=0x1ABC9C)

        response_jeu.set_footer(text=f'En réponse à {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        response_jeu.add_field(name="Je sais pas si je t'adore", value="Allez , si tu m'adores en tant que bot préféré, met la réaction 👍 (ou si je suis pas ton bot préféré alors attends que je réponde.)", inline=False)
        await ctx.send(embed=response_jeu)
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await bot.client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("👎 oh ben je suis décu...")
        else:
            await ctx.send("👍 ha un nouveau pote !")

    @commands.command(description="Un bon vieux pile ou face")
    async def pile_ou_face(self, ctx):
        response_jeu = discord.Embed(title='Pile ou face', color=0xF1C40F)

        response_jeu.set_footer(text=f'En réponse à {ctx.message.author.name}',
                                icon_url=ctx.message.author.avatar_url)
        pile_ou_face = random.randint(1, 2)
        if pile_ou_face == 1:
            response_jeu.add_field(name='Pile , ou face ?', value="La pièce est tombé sur... pile !", inline=False)
            await ctx.send(embed=response_jeu)
        elif pile_ou_face == 2:
            response_jeu.add_field(name='Pile , ou face ?', value="La pièce est tombé sur... face !", inline=False)
            await ctx.send(embed=response_jeu)
# On lance la classe

def setup(client):
    client.add_cog(Jeux(client))