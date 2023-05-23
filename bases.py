
from random import randint, choice
from discord.ext import commands
from pathlib import Path
import textwrap


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

    @commands.command()
    async def test(self, ctx):
        respond = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur et commodo lacus, eget pulvinar " \
                  "libero. Vestibulum eget tortor est. Duis in feugiat urna, malesuada tempor lacus. Nulla pharetra " \
                  "lectus turpis. Proin turpis enim, dictum quis molestie a, condimentum sit amet purus. Ut tempor " \
                  "luctus turpis non suscipit. Proin mi leo, facilisis id tempus eu, tempus vel leo. Phasellus " \
                  "volutpat nulla vel metus commodo, at pellentesque ex rhoncus. Morbi congue pulvinar lobortis. Nunc " \
                  "dapibus, sapien in semper suscipit, nisi ante suscipit neque, a malesuada augue lacus sed mauris. " \
                  "Pellentesque non elit ac orci efficitur porttitor eget in turpis. Fusce quis quam ut odio " \
                  "scelerisque pharetra. Sed egestas aliquet est, id blandit ante malesuada et. Integer aliquet sit " \
                  "amet augue eget dictum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames " \
                  "ac turpis egestas.Vivamus in congue tellus. Morbi tincidunt ornare est a ultricies. Cras tincidunt " \
                  "est eu vulputate imperdiet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam " \
                  "vulputate suscipit sodales. Sed ultricies neque vitae libero blandit gravida. Donec lobortis, " \
                  "ante eu finibus porttitor, ex odio fermentum mi, nec molestie neque eros eu dolor. Curabitur " \
                  "tincidunt ornare dui vitae malesuada. Quisque in augue tincidunt, gravida mi id, scelerisque arcu. " \
                  "Vestibulum nec suscipit mi. Donec venenatis posuere mi, in feugiat erat vestibulum at. Curabitur " \
                  "dapibus ligula sapien, eget pulvinar neque congue nec.Curabitur dictum erat nisl, sed molestie est " \
                  "ultricies in. Proin fringilla lobortis fringilla. In in urna cursus, mattis diam in, " \
                  "placerat justo. Etiam sagittis ex vitae risus laoreet pulvinar. Nulla dapibus orci vitae eros " \
                  "congue pharetra ac vel lacus. Vivamus lacinia mauris eu leo viverra, eget posuere urna rhoncus. " \
                  "Nulla facilisi. Nunc ex orci, sollicitudin nec semper ac, posuere sit amet urna. Phasellus viverra " \
                  "molestie ipsum, et ornare nibh consequat eu. Vestibulum suscipit tincidunt ligula at semper. " \
                  "Praesent finibus quam at justo ultricies pretium. Etiam at metus ipsum.Nunc scelerisque nisl " \
                  "metus, vitae fermentum enim feugiat sit amet. Donec rhoncus vulputate diam, eu efficitur erat " \
                  "mattis et. Proin pharetra condimentum sem in molestie. Lorem ipsum dolor sit amet, consectetur " \
                  "adipiscing elit. Mauris ac ligula nibh. Vivamus elit dui, lobortis placerat ante in, cursus ornare " \
                  "massa. Proin finibus cursus lacus eget ultrices. Proin mattis lectus risus, ac suscipit diam " \
                  "fringilla vitae. Nam non vulputate quam.Curabitur vitae aliquet nisl, sit amet consectetur dui. " \
                  "Praesent non tempus nisi. Curabitur interdum, massa in congue pharetra, massa dolor placerat elit, " \
                  "vel malesuada augue nibh at massa. Vivamus nisl lorem, vulputate sed sollicitudin in, " \
                  "finibus pretium massa. Mauris in diam maximus, porta augue quis, convallis risus. Nam purus ipsum, " \
                  "elementum vitae lacus vitae, pellentesque vulputate ante. Nunc ut laoreet enim, nec dignissim " \
                  "velit. Ut orci nunc, pharetra eu magna eget, interdum tempus massa. Curabitur lobortis odio non " \
                  "quam ullamcorper aliquam. Nullam suscipit scelerisque feugiat.Mauris non orci est. Donec libero " \
                  "ex, venenatis a neque a, tristique condimentum mi. Curabitur fermentum dapibus neque eu aliquam. " \
                  "Nulla quis quam enim. Donec vehicula auctor mi sed efficitur. Nam ac ante at ex egestas gravida. " \
                  "Nam imperdiet libero eget odio egestas sagittis. Vivamus molestie accumsan sapien, id volutpat " \
                  "enim ullamcorper sed. Quisque et turpis id nulla aliquam tristique. Maecenas eu tincidunt nisi. " \
                  "Curabitur facilisis odio in pretium fringilla. Duis congue ullamcorper ultrices.Ut facilisis " \
                  "rutrum nisi et suscipit. In leo ligula, sodales id feugiat sit amet, mattis quis arcu. Curabitur " \
                  "ut nibh pulvinar, placerat orci ac, lacinia tellus. Proin vitae eros ac nisl accumsan sollicitudin " \
                  "accumsan vitae arcu. Sed efficitur nec lectus in facilisis. Nulla accumsan augue diam. " \
                  "Pellentesque et luctus nibh, sit amet ornare odio. Curabitur lacinia leo at enim volutpat! "

        chunks = textwrap.wrap(respond, width=2000)

        # Send each chunk as a separate message
        for chunk in chunks:
            await ctx.send(chunk)
