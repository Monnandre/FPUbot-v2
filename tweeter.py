from discord.ext import commands
import tweepy
import os


class tweeter_cog(commands.Cog):
    def __init__(self, bot):
        api_key_tweeter = str(os.environ['api_key_tweeter'])
        self.bot = bot
        # for tweeter
        self.auth = tweepy.OAuthHandler(
            "TSwu7v8MYWfKADNUy5LxdoxjQ",
            "ZTxg0LcaQh4kFgPqY1kPvNzxp13uY19WpNypZjK2wb6ccz21BN")
        self.auth.set_access_token(api_key_tweeter,
                                   "w2EYk8oYC9QCbLDmTiOqK8A3W5PJqxX34xcix6CjdxfKi")

        self.api = tweepy.API(self.auth)

    @commands.command(name="games")
    async def gotoXbox(self, ctx):
        await ctx.channel.send("https://twitter.com/XboxGamePassFR")

    @commands.command(name="films")
    async def gotoNetfix(self, ctx):
        await ctx.channel.send("https://twitter.com/NetflixFR")

    @commands.command(name="find")
    async def gotoSomeOne(self, ctx, name):
        await ctx.channel.send(f"https://twitter.com/{name}")

    @commands.command(name="tweet")
    async def search(self, ctx, number: int = 1, *args):
        query = " ".join(args)
        tweets = tweepy.Cursor(self.api.search_tweets, q=query).items(number)
        for tweet in tweets:
            Tweetid = tweet.id
            mots = str(tweet.text).split(' ')
            for mot in mots:
                if mot[0] == '@':
                    nom = mot[:-1]
                    break
            try:
                await ctx.channel.send(f"https://twitter.com/{nom}/status/{Tweetid}")
            except:
                await ctx.channel.send(tweet.text)

    @commands.command(name="trend")
    async def shearch_Trends(self, ctx, number: int = 1):
        nbTrends = 0
        nbMax = number
        woeid = 610264
        trends = self.api.get_place_trends(woeid)
        for value in trends:
            for trend in value['trends']:
                if nbTrends < nbMax:
                    await ctx.channel.send(trend['name'])
                    nbTrends += 1
