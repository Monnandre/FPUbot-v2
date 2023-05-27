

import discord
from discord.ext import commands
from tweeter import tweeter_cog
from bases import bases_cog
from addons import addons_cog
from AI import ai_cog
from leaders import leaderboard_cog
import os
import asyncio


api_key_bot = str(os.environ['api_key_bot'])

command_prefix = "!"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=command_prefix, intents=intents)
bot.remove_command('help')

async def setup():
    await bot.add_cog(tweeter_cog(bot))
    await bot.add_cog(bases_cog(bot))
    await bot.add_cog(addons_cog(bot))
    await bot.add_cog(ai_cog(bot))
    await bot.add_cog(leaderboard_cog(bot))

asyncio.run(setup())
@bot.event
async def on_ready():
    print('Logged in as :', bot.user.name)
    print('Bot ID :', bot.user.id)
    print('------')


@bot.event
async def on_command_error(ctx, exc):
    if isinstance(exc, commands.CommandNotFound):
        await ctx.channel.send(f"{command_prefix}help est sans doute nécessaire...")
    if isinstance(exc, commands.MissingRequiredArgument):
        await ctx.channel.send("Il manque un argument...")

@bot.command(aliases=["h", "aled"])
async def help(ctx, key=None):
    embed = discord.Embed(colour=discord.Colour.green())
    if key is None:
        embed.set_author(name='Liste des commandes de bases :')
        # Commandes User
        embed.add_field(name=f"**{command_prefix}help admin**", value="Commandes Admin", inline=False)
        embed.add_field(name=f"**{command_prefix}help twitter**", value="Commandes Twitter", inline=False)
        embed.add_field(name=f"**{command_prefix}ping**", value="Mesurer la latence", inline=False)
        embed.add_field(name=f"**{command_prefix}piece**", value="Pile ou face", inline=False)
        embed.add_field(name=f"**{command_prefix}random x**", value="Choisir un nombre entre 1 et x, alias: r", inline=False)
        embed.add_field(name=f"**{command_prefix}test**", value="Un truc random en fonction de ce que je suis entrain de tester", inline=False)
        embed.add_field(name=f"**{command_prefix}lb name**", value="Renvoie le leaderboard de V-Spin. Possibilites: les noms des modes de jeu (avec une majuscule), Coins et Time", inline=False)

    elif key == "twitter":
        embed.set_author(name='Liste des commandes de twitter :')
        # Commandes
        embed.add_field(name=f"**{command_prefix}games**", value="Xbox", inline=False)
        embed.add_field(name=f"**{command_prefix}films**", value="Netfix", inline=False)
        embed.add_field(name=f"**{command_prefix}find name**", value="Trouver quelqu'un", inline=False)
        embed.add_field(name=f"**{command_prefix}tweet x [keywords]**", value="Trouver un tweet", inline=False)
        embed.add_field(name=f"**{command_prefix}trend n**", value="Connaitre le top n trends de Marseille", inline=False)

    elif key == "admin":
        embed.set_author(name='Liste des commandes de admin :')
        # Commandes
        embed.add_field(name=f"**{command_prefix}del x**", value="Suppression de x messages", inline=False)
        embed.add_field(name=f"**{command_prefix}animate**", value="Une IA envoie un message toute les heures", inline=False)
        embed.add_field(name=f"**{command_prefix}new_prompt [phrase]**", value="Modifie le prompt, alias: np", inline=False)
        embed.add_field(name=f"**{command_prefix}set_memory [phrase]**", value="Modifie la memoire, alias: sm",
                        inline=False)
        embed.add_field(name=f"**{command_prefix}spam @ x [phrase]**", value="Spam @ de x messages contenant phrase en privé",inline=False)

    elif key == "ai":
        embed.set_author(name="Liste des commandes d\'AI :")
        # Commandes
        embed.add_field(name=f"**{command_prefix}prompt**", value="Envoie le prompt actuel du bot", inline=False)
        embed.add_field(name=f"**{command_prefix}memory**", value="Envoie la memoire actuele du bot", inline=False)
        embed.add_field(name=f"**{command_prefix}aigame**", value="Un jeu pour casser les AI", inline=False)

    else:
        await ctx.send("L' argument est incorect")
    await ctx.send(embed=embed)

@bot.command(aliases=["del"])
@commands.guild_only()
@commands.has_role('modérateur')
async def delete(ctx, number: int):
    await ctx.channel.purge(limit=number + 1)


bot.run(api_key_bot)
