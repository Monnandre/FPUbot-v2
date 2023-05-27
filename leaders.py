
from playfab import PlayFabClientAPI, PlayFabSettings
from discord.ext import commands



class leaderboard_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        PlayFabSettings.TitleId = "F44F3"
        login_request = {
            "CustomId": "GettingStartedGuide",
            "CreateAccount": True
        }
        PlayFabClientAPI.LoginWithCustomID(login_request, self.login_callback)
        self.ctx = None
        self.leaderboard = {}

    def login_callback(self, success, failure):
        if success:
            print("Leaderboard login")
        else:
            print("Something went wrong with your first API call.  :(")
            if failure:
                print("Here's some debug information:")
                print(failure)

    def leaderboard_callback(self, success, failure):
        if success:
            self.leaderboard = success["Leaderboard"]
        else:
            print("Something went wrong with your first API call.  :(")
            if failure:
                print("Here's some debug information:")
                print(failure)

    @commands.command()
    async def lb(self, ctx, name: str):
        self.leaderboard = {}
        self.ctx = ctx
        request_leaderboard = {
            "StatisticName": name,
            "StartPosition":0,
            "MaxResultsCount": 5
        }

        # Make the API call and pass in the callback_wrapper function
        PlayFabClientAPI.GetLeaderboard(request_leaderboard, self.leaderboard_callback)
        if self.leaderboard:
            for entry in self.leaderboard:
                if entry.get("DisplayName", False):
                    await self.ctx.send(f"{entry['Position'] + 1}: {entry['DisplayName']} - {entry['StatValue']}")
                else:
                    await self.ctx.send(f"{entry['Position'] + 1}: {entry['PlayFabId']} - {entry['StatValue']}")
