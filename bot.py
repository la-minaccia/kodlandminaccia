import discord, random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

with open('token.txt', 'r', encoding='utf-8') as f:
    TOKEN = f.read()


#with open('images/cat.jpg', 'rb') as f:
#        picture = discord.File(f)

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def leggi(ctx):
    # leggere il file di testo
    with open('text.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command()
async def scrivi(ctx, testo: str):
    # leggere il file di testo
    with open('text.txt', 'a', encoding='utf-8') as f:
        #text = "sto modificando il file di testo"
        f.write(testo)
        await ctx.send(f"modficato il file di testo con: {testo}")
        print(testo)

@bot.command()
async def mem(ctx):
    name = random.choice(os.listdir('images'))
    with open(f'images/{name}', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memes(ctx, alias: str):
    try:
        with open(f'images/{alias}.png', 'rb') as f:
            # Memorizziamo il file della libreria di Discord convertito in questa variabile!
            picture = discord.File(f)
        await ctx.send(file=picture)
    except Exception:
        await ctx.send('Memes non trovato! I meme disponibili sono: meme1, meme2, meme3')

# INQUINAMENTO

@bot.command()
async def inquinamento1(ctx):
    lista_inquinamento = ['buttare la plastica inquina', 'i razzi creano inquinamento', 'le auto inquinano', 'l\'industria inquina', 'l\'inquinamento fa male alla salute']
    await ctx.send(random.choice(lista_inquinamento))

@bot.command()
async def inquinamento2(ctx):
    with open('inquinamento.txt', 'r', encoding='utf-8') as f:
        inquinamento = f.read()
    await ctx.send(inquinamento)

@bot.command()
async def inquinamento3(ctx):
    with open('images/plastica.png','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def inquinamento(ctx):
    val = random.randint(1,3)
    if val == 1: inquinamento1(ctx)
    if val == 2: inquinamento2(ctx)
    if val == 3: inquinamento3(ctx)



bot.run(TOKEN)
