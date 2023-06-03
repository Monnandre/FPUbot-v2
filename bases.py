
from random import randint, choice
from discord.ext import commands
import discord
from pathlib import Path
import textwrap
import asyncio


class bases_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.path = Path(__file__).parent.resolve()

    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send("Pong!")

    @commands.command()
    async def piece(self, ctx):
        message = await ctx.channel.send("Pile 🔋 ou face 😉")
        await message.add_reaction("🔋")
        await message.add_reaction("😉")

        def checkReact(react, user):
            return ctx.message.author == user and ctx.message.author != self.bot.user.id \
                   and message.id == react.message.id and (str(react.emoji) == "🔋") or (str(react.emoji) == "😉")

        reaction, user = await self.bot.wait_for("reaction_add",
                                                 timeout=10,
                                                 check=checkReact)
        choix = ["Gagné !", "Perdu !"]

        if reaction.emoji == "🔋":
            await ctx.channel.send("Votre choix : Pile")
            await ctx.channel.send(choice(choix))
        elif reaction.emoji == "😉":
            await ctx.channel.send("Votre choix : Face")
            await ctx.channel.send(choice(choix))

    @commands.command(name="random", aliases=["r"])
    async def lancer(self, ctx, number: int):
        choix = randint(1, number)
        await ctx.channel.send(choix)

    @commands.guild_only()
    @commands.has_role('modérateur')
    @commands.command(name="send", aliases=["s"])
    async def send_message_as_bot(self, ctx, destination_channel, *args):
        message = " ".join(args)
        channel_id = int(destination_channel.strip("<#").strip(">"))
        channel = discord.utils.get(ctx.guild.text_channels, id=channel_id)
        if channel is None:
            await ctx.send("I couldn't find that channel.")
            return
        await channel.send(message)

    @commands.guild_only()
    @commands.has_role('modérateur')
    @commands.command(name="send_delayed", aliases=["sd"])
    async def send_delayed_message_as_bot(self, ctx, destination_channel, delay, *args):
        message = " ".join(args)
        channel_id = int(destination_channel.strip("<#").strip(">"))
        channel = discord.utils.get(ctx.guild.text_channels, id=channel_id)
        if channel is None:
            await ctx.send("I couldn't find that channel.")
            return


        try: delay = float(delay)
        except:
            await ctx.send("Wrong delay format. Send int or float in the form 1.0")
            return

        await asyncio.sleep(delay * 60)
        await channel.send(message)

    @commands.command()
    async def test(self, ctx):
        print(type(ctx.message.author) == discord.Message)
