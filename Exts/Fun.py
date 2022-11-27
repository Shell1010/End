from selfcord import Extender
import asyncio



class Ext(Extender, name="Fun", description="Fun commands"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @Extender.cmd(description="Spam calls people", aliases=['ring'])
    async def call(self, ctx):
        await ctx.message.delete()
        for i in range(10):
            await ctx.channel.call()
            await asyncio.sleep(1.7)
            await ctx.channel.leave()