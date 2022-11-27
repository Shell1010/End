from selfcord import Extender
import aiohttp




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

    @Extender.cmd(description="Gathers token information", aliases=['tdox', 'tinfo'])
    async def tokeninfo(self, ctx, _token):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://discord.com/api/v9/users/@me", headers={"authorization": _token}) as resp:
                if resp.status == 200:
                    data = await resp.json()

                    msg = f"```diff\n+ Token Information\n"
                    for key, value in data.items():
                        msg += f"- {key}:   {value}\n"
                    msg += "```"
                    return await ctx.reply(msg)
                else:
                    async with session.get("https://discord.com/api/v9/users/@me", headers={"authorization": f"Bot {_token}"}) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            msg = f"```diff\n+ Token Information\n"
                            for key, value in data.items():
                                msg += f"- {key}:   {value}\n"
                            msg += "```"
                            return await ctx.reply(msg)
                        else:
                            data = await resp.json()
                            return await ctx.reply(f"```\n{data}```")
       
