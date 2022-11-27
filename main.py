import selfcord
import json
import os
from colorama import Fore as color
import asyncio

with open("./config.json") as f:
    config = json.load(f)

prefixes = config['prefixes']
token = config['token']

bot = selfcord.Bot(prefixes=prefixes, inbuilt_help=False)

@bot.on("ready")
async def ready(time):
    for item in os.listdir("./Exts"):
        if item.endswith(".py"):
            await bot.load_extension(f"Exts.{item[:-3]}")
            print(f"{color.LIGHTGREEN_EX}Extension loaded: {item}")
    await asyncio.sleep(1.5)
    # os.system('cls' if os.name=='nt' else 'clear')
    await bot.change_presence(status="dnd", activity=selfcord.Activity.Stream("OMEGA", "We Sexy", "OMEGA", buttons={"Join OMEGA": "https://discord.gg/JA7YJEgkkP", "Join Selfcord": "https://discord.gg/VTm26arz9Z"}))
    print(f"""{color.BLUE}

▓█████  ███▄    █ ▓█████▄
▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒███   ▓██  ▀█ ██▒░██   █▌
▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
░▒████▒▒██░   ▓██░░▒████▓
░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒
 ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒
   ░      ░   ░ ░  ░ ░  ░
   ░  ░         ░    ░
                   ░
{color.LIGHTRED_EX}__________________________

CONNECTED TO:
USER: {bot.user}
GUILDS: {len(bot.user.guilds)}
FRIENDS: {len(bot.user.friends)}
STARTUP:  {time:0.2f} seconds{color.RESET}""")

@bot.on("error")
async def error_log(e):
    print(e)

@bot.cmd(description="Help command <category>")
async def help(ctx, cat: str=None):

    if cat is None:
        msg = f"```ini\n"
        msg += f"[ end ]\n\n[ Prefixes ] = {bot.prefixes}\n\n"
        msg += f"<> = argument\n\n"
        for ext in bot.extensions:
            msg += f"[ .{ext.name} ] {ext.description}\n"
        for command in bot.commands:
            msg += f".{command.name}:    {command.description}\n"

            if len(msg) > 1980:
                msg += f"```"
        msg += f"```"
        return await ctx.reply(f"{msg}")

    else:
        name = cat.lower()
        for ext in bot.extensions:
            if name == ext.name.lower():
                msg = f"```ini\n"
                msg += f"[ {ext.name} ] - {ext.description}\n[ Prefixes ]   {bot.prefixes}\n\n"
                msg += f"<> = argument\n\n"

                for command in ext.commands:
                    msg += f".{command.name}:    {command.description}\n"
                msg += f"```"
                return await ctx.reply(f"{msg}")
bot.run(token)
