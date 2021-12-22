import discord
import aiohttp
from discord.ext import commands
from discord.commands import slash_command


class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(guild_ids=[918349390995914792], description="Get a random fox fact along with a picture!")
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://randomfox.ca/floof/") as r:
                data = await r.json()
                image_url = data["image"]
            
            async with cs.get("https://some-random-api.ml/facts/fox") as r:
                data = await r.json()
                fact_url = data["fact"]

                embed = discord.Embed(title="🦊", description=fact_url, colour=ctx.author.colour)
                embed.set_image(url=image_url)
                embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

                await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[918349390995914792], description="Get a random dog fact along with a picture!")
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                data = await r.json()
                image_url = data["message"]
            
            async with cs.get("https://some-random-api.ml/facts/dog") as r:
                data = await r.json()
                fact_url = data["fact"]

                embed = discord.Embed(title="Woof! 🐶", description=fact_url, colour=ctx.author.colour)
                embed.set_image(url=image_url)
                embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

                await ctx.respond(embed=embed)

    @slash_command(guild_ids=[918349390995914792], description="Get a random cat fact along with a picture!")
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/cat") as r:
                data = await r.json()
                image_url = data["link"]
            
            async with cs.get("https://some-random-api.ml/facts/cat") as r:
                data = await r.json()
                fact_url = data["fact"]

                embed = discord.Embed(title="Meow 😻", description=fact_url, colour=ctx.author.colour)
                embed.set_image(url=image_url)
                embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

                await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[918349390995914792], description="Get a random panda fact along with a picture!")
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animal/panda") as r:
                data = await r.json()

                embed = discord.Embed(title="🐼", description=data["fact"], colour=ctx.author.colour)
                embed.set_image(url=data["image"])
                embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

                await ctx.respond(embed=embed)

    @slash_command(guild_ids=[918349390995914792], description="Get a random koala fact along with a picture!")
    async def koala(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animal/koala") as r:
                data = await r.json()

                embed = discord.Embed(title="🐨", description=data["fact"], colour=ctx.author.colour)
                embed.set_image(url=data["image"])
                embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

                await ctx.respond(embed=embed)

    @slash_command(guild_ids=[918349390995914792], description="Get a random bird fact along with a picture!")
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animal/birb") as r:
                data = await r.json()

                embed = discord.Embed(title="🐦", description=data["fact"], colour=ctx.author.colour)
                embed.set_image(url=data["image"])
                embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

                await ctx.respond(embed=embed)

    @slash_command(guild_ids=[918349390995914792], description="Get a random raccoon fact along with a picture!")
    async def raccoon(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animal/raccoon") as r:
                data = await r.json()

                embed = discord.Embed(title="🦝", description=data["fact"], colour=ctx.author.colour)
                embed.set_image(url=data["image"])
                embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

                await ctx.respond(embed=embed)

    @slash_command(guild_ids=[918349390995914792], description="Get a random kangaroo fact along with a picture!")
    async def kangaroo(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animal/kangaroo") as r:
                data = await r.json()

                embed = discord.Embed(title="🦘", description=data["fact"], colour=ctx.author.colour)
                embed.set_image(url=data["image"])
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

                await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Animals(bot)) 