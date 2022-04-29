import discord
from discord import app_commands
from discord.ext import commands
from utils.views import CreateRole, DeleteRole 
import re
from discord.app_commands import checks, MissingPermissions


class Role(commands.Cog,app_commands.Group,name="role"):
    """For Role Management"""
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()


    @app_commands.command(name="create",description="Create a role")
    @checks.has_permissions(manage_roles=True)
    async def create(self,interaction: discord.Interaction,name:str,color:str=None):
        if color==None:
            view=CreateRole()
            view.rolen=name
            view.guild=interaction.guild
            embed=discord.Embed(title="Confirm?", description=f"Please confirm that you really want to create `{name}`", color=0x00eeff)
            await interaction.response.send_message(embed=embed,view=view)
        
        elif color:
            view=CreateRole()
            view.rolen=name
            view.guild=interaction.guild
            view.rolec = color
            embed=discord.Embed(title="Confirm?", description=f"Please confirm that you really want to create `{name}` with color `{color}`",color=discord.Colour.from_str(color))
            await interaction.response.send_message(embed=embed,view=view)

        else:
            await interaction.response.send_message("Invalid color (make sure u send a hex color code)")


    @app_commands.command(name="delete", description="Delete any pre-existing role from server")
    @checks.has_permissions(manage_roles=True)
    async def delete(self,interaction:discord.Interaction,role:discord.Role,reason:str=None):
        view = DeleteRole() 
        view.role=role
        name = role.name
        view.value=name
        embed=discord.Embed(title="Confirm?", description=f"Please confirm that you really want to delete {role.mention}", color=0xff0000)
        await interaction.response.send_message(embed=embed,view=view)
        

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Role(bot), guilds=[discord.Object(id=)])
