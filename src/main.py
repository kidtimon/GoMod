from wsgiref.util import application_uri
import discord
from discord.ext import commands
from utils.views import *
from discord import app_commands, Interaction
from discord.app_commands import AppCommandError, Command, ContextMenu
from typing import Union
from config import config

class GoMod(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=".",
            intents=discord.Intents.default(),
            application_id=config.application_id
        )

    async def setup_hook(self):
        await self.load_extension("cogs.roles")
        #await self.load_extension("cogs.cerror")
        await bot.tree.sync(guild = discord.Object(id=config.guild_id))

    async def on_ready(self):
        print("Successfully synced commands")
        print(f"Logged")    
        


bot=GoMod()
        
bot.run(config.token)

    
