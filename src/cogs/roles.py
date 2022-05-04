from dataclasses import replace
from math import perm
import discord
from discord import app_commands
from discord.ext import commands
from utils.views import CreateRole, DeleteRole, GiveRole, RemoveRole 
import re
from discord.app_commands import checks, MissingPermissions
from config import config

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
    
    @app_commands.command(name="give",description="Give a role")
    @checks.has_permissions(manage_roles=True)
    async def give(self, interaction:discord.Interaction,user:discord.Member,role:discord.Role):
        view = GiveRole()
        view.user=user
        view.role=role

        if role in user.roles:
            await interaction.response.send_message(f"That user already have {role.mention} role",ephemeral=True)
        else:
            embed=discord.Embed(title="Confirm?", description=f"You are about to give {role.mention} to {user.mention}", color=0xff0000)
            await interaction.response.send_message(embed=embed,view=view)

    @app_commands.command(name="remove", description="Remove a role")
    @checks.has_permissions(manage_roles=True)
    async def remove(self, interaction:discord.Interaction, user:discord.Member, role:discord.Role):
        view = RemoveRole()
        view.user=user
        view.role=role
        if role not in user.roles:
            await interaction.response.send_message(f"That user don't have {role.mention} role",ephemeral=True)
        else:
            embed=discord.Embed(title="Confirm?", description=f"You are about to remove {role.mention} from {user.mention}", color=0xff0000)
            await interaction.response.send_message(embed=embed,view=view)

    @app_commands.command(name="info",description="Get information about any particular role.")
    async def info(self,interaction:discord.Interaction,role:discord.Role):
            embed=discord.Embed(title="Role Info",color=role.color)
            embed.add_field(name="Name", value=role.name, inline=True)
            embed.add_field(name="ID", value=role.id, inline=True)    
            embed.add_field(name="Members", value=len(role.members), inline=True)
            embed.add_field(name="Position", value=role.position, inline=True)
            embed.add_field(name="Mentionable", value=role.mentionable, inline=True)
            embed.add_field(name="Hoisted", value=role.hoist, inline=True)
            embed.add_field(name="Managed", value=role.managed, inline=True)
            embed.add_field(name="Color", value=role.color, inline=True)
            embed.add_field(name="Creation Date", value=f"{role.created_at.strftime('%a, %#d %B %Y, %I:%M %p')}", inline=True)
            perms = [perm for perm, _bool in role.permissions if _bool is True]
            perms = [perms.replace("_"," ").title().replace("Tts","TTS") for perms in perms]
            finalp = ', '.join(perms)
            embed.add_field(name="Permissions", value=finalp, inline=True)
            embed.set_footer(text=f"Requested by {interaction.user.name}#{interaction.user.discriminator}",icon_url=interaction.user.display_avatar)
            await interaction.response.send_message(embed=embed)
        

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Role(bot), guilds=[discord.Object(id=config.guild_id)])
