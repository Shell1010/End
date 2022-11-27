from selfcord import Extender




class Ext(Extender, name="Util", description="General utility commands"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.afk_arg = False
        self.afk_message = ""


    @Extender.cmd(description="Purge messages")
    async def purge(self, ctx, amount: int=None):
        await ctx.message.delete()
        await ctx.purge(amount)

    @Extender.cmd(description="Testing ")
    async def Util(self, ctx):
        await ctx.message.delete()
        print(self, self.__dict__)

    @Extender.cmd(description="Sets user to AFK")
    async def afk(self, ctx, *, message):
        self.afk_arg = True
        self.afk_message = message
        await ctx.reply(f"```ini\n[ AFK ] - {message}```")

    @Extender.on("message")
    async def afk_check(self, message):
        if self.afk_arg:
            if self.bot.user.id in message.content:
                msg = f"```ini\n[ AFK ] - {self.afk_message}```"
                await message.channel.reply(msg)
            if self.bot.user.id in message.author.id:
                msg = f"```ini\n[ No Longer AFK ] - {self.afk_message}```"
                await message.channel.reply(msg)
                self.afkk = False
