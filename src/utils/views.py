import discord
from discord.ui import View 

class CreateRole(View):
    def __init__(self):
        super().__init__()
        self.rolen=None
        self.guild=None
        self.rolec=None

    @discord.ui.button(label="Confirm",style=discord.ButtonStyle.green)
    async def confirm_callback(self,button:discord.ui.Button,interaction:discord.Interaction):
        if self.rolec==None:
            role = await self.guild.create_role(name=self.rolen)
            embed=discord.Embed(title="Role Created", description=f"Successfully created {role.mention}", color=0x00ff04)
            await button.response.edit_message(embed=embed,view=None)
        if self.rolec:
            role = await self.guild.create_role(name=self.rolen,color=discord.Colour.from_str(self.rolec))
            embed=discord.Embed(title="Role Created", description=f"Successfully created {role.mention}", color=discord.Colour.from_str(self.rolec))
            await button.response.edit_message(embed=embed,view=None)
            

    
    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline_callback(self,button:discord.ui.Button,interaction:discord.Interaction):  
        embed=discord.Embed(title="Denied", description=f"Creation of role `{self.value}` was denied", color=0xff0000)
        await button.response.edit_message(embed=embed,view=None)


class DeleteRole(View):
    def __init__(self):
        super().__init__()
        self.value=None
        
    @discord.ui.button(label="Confirm",style=discord.ButtonStyle.green)
    async def confirm_callback(self,button:discord.ui.Button,interaction:discord.Interaction):
        self.role.delete
        embed=discord.Embed(title="Role Deleted", description=f"Successfully deleted `{self.value}`", color=0x00ff04)
        await button.response.edit_message(embed=embed,view=None)



    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline_callback(self,button:discord.ui.Button,interaction:discord.Interaction):  
        embed=discord.Embed(title="Denied", description=f"Removal of role was denied", color=0xff0000)
        await button.response.edit_message(embed=embed,view=None)

