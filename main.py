import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)


TOKEN = "Tu Token aqui"

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

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def meme(ctx):
    imagenes = os.listdir('images')
    seleccion = random.choice(imagenes)
    with open(f'images/{seleccion}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck,
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run(TOKEN)
