import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
bot = commands.Bot(command_prefix="/", intents=intents)


TOKEN = "Token de tu bot" 

@bot.event
async def on_ready():
    print(f"Se conectado como{bot.user}")
@bot.command()
async def hola(ctx):
        await ctx.send(f"!Hola {ctx.author.name}✌️")

@bot.event
async def on_member_join(member):
      for channel in member.guild.text_channels:
            if channel.permissions_for(member.guild.me).send_message:
             await   channel.send(f"!Bienvenido {member.mention}🎉")   
             
             break
            
@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run(TOKEN)