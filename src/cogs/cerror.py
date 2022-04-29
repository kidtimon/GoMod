"""
import discord
from discord.ext import commands
from discord import app_commands, Interaction
from discord.app_commands import AppCommandError, Command, ContextMenu
from typing import Union


class DebugErrors(commands.Cog):
    #Console Error Handl
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    
async def global_app_command_error_handler(bot: commands.Bot):
    @bot.tree.error
    async def app_command_error(
            interaction: Interaction,
            error: AppCommandError
    ):
        if isinstance(error, app_commands.CommandInvokeError):
            print(error.original, error.command)

        elif isinstance(error, app_commands.TransformerError):
            print(error.value, error.type, error.transformer)

        elif isinstance(error, app_commands.CheckFailure):
            if isinstance(error, app_commands.NoPrivateMessage):
                pass
            elif isinstance(error, app_commands.MissingRole):
                print(error.missing_role)
            elif isinstance(error, app_commands.MissingAnyRole):
                for role in error.missing_roles:
                    print(role)
            elif isinstance(error, app_commands.MissingPermissions):
                for permission in error.missing_permissions:
                    print(permission)
            elif isinstance(error, app_commands.BotMissingPermissions):
                for permission in error.missing_permissions:
                    print(permission)
            elif isinstance(error, app_commands.CommandOnCooldown):
                print(error.cooldown, error.retry_after)

        elif isinstance(error, app_commands.CommandLimitReached):
            print(error.type, error.guild_id, error.limit)

        elif isinstance(error, app_commands.CommandAlreadyRegistered):
            print(error.name, error.guild_id)

        elif isinstance(error, app_commands.CommandSignatureMismatch):
            print(error.command)

        elif isinstance(error, app_commands.CommandNotFound):
            print(error.name, error.parents, error.type)


async def setup(bot: commands.Bot) -> None:
    await global_app_command_error_handler(bot=bot)
    await bot.add_cog(DebugErrors(bot), guilds=[discord.Object(id=)])

"""
