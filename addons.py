from discord.ext import commands
import discord


class addons_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="spam")
    @commands.guild_only()
    @commands.has_role('modérateur')
    async def spamSomeone(self, ctx, mention: discord.Member, nb=5, *args):
        text = " ".join(args)
        await ctx.channel.send("ok")
        for _ in range(nb):
            await mention.send(text)
        await ctx.channel.send("done")