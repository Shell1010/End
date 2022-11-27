from selfcord import Extender

class Ext(Extender, name="User", description="User related utility commands"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @Extender.cmd(description="Gathers user information <user>", aliases=["userinfo", "info"])
    async def whois(self, ctx, user_id: str):
        msg = "```ini\n"
        user = await self.bot.get_user(user_id)
        profile = await user.get_profile()
        msg += f"[ Username ] - {user}\n[ ID ] - {user.id}\n[ Bot? ] - {user.bot_acc}\n[ Created At ] - {user.created_at}\n[ Base64 Token ] - {user.b64token}\n[ Bio ]\n{profile.bio}\n\n"
        msg += f"[ Mutual Guilds ]\n\n"
        try:
            for guild in profile.mutual_guilds:
                msg += f"   - [ {guild.name} ]\n"
        except:
            msg += f"None\n"

        msg += f"\n[ Connected Accounts ]\n\n"
        try:
            for account in profile.connected_accounts:
                msg += f"   [ {account.type} ] - {account.name}\n"
        except:
            msg += f"None\n"

        msg += f"\n[ Premium Type ] - {profile.premium_type}\n```"

        avatar = user.avatar_url
        banner = user.banner_url
        msg += f"AVATAR: {avatar}\nBANNER: {banner}"
        await ctx.reply(msg)

    @Extender.cmd(description="Steals a users pfp <user>", aliases=['getpfp'])
    async def stealpfp(self, ctx, id: str):
        user = await self.bot.get_user(id)
        await self.bot.change_pfp(user.avatar_url)
        await ctx.reply("Successfully changed pfp")

    @Extender.cmd(description="Sets pfp as specified url <url>")
    async def setpfp(self, ctx, url: str):
        await self.bot.change_pfp(url)
        await ctx.reply("Successfully changed pfp")

    @Extender.cmd(description="Adds users as friend <user>", aliases=["addfriend"])
    async def friend(self, ctx, id: str):
        await self.bot.add_friend(id)
        await ctx.reply("Successfully sent request")

    @Extender.cmd(description="Displays Avatar <user>", aliases=['av', 'pfp'])
    async def avatar(self, ctx, id: str):
        user = await self.bot.get_user(id)
        await ctx.reply(f"{user.avatar_url}")

    @Extender.cmd(description="Change Bio")
    async def bio(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.edit_profile(bio=message)

    @Extender.cmd(description="Testing ")
    async def User(self, ctx):
        await ctx.message.delete()
        print(self, self.__dict__)

