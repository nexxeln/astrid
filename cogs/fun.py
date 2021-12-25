import discord
import requests
import aiohttp
from settings import API_NINJAS_KEY
from discord.ext import commands
from discord.commands import slash_command, Option
from PIL import Image, ImageFilter
from io import BytesIO

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[918349390995914792], description="Emojify a message")
    async def emojify(self, ctx, text: Option(str, "Enter your message", required=True, default="astrid")):
        emojis = []
        for char in text:
            if char.isdecimal():
                num_to_emoji = {
                    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
                    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
                }
                emojis.append(f":{num_to_emoji.get(char)}:")

            elif char.isalpha():
                emojis.append(f":regional_indicator_{char}:")
    
            elif char in "?!#+-":
                special_char_to_emoji = {
                    "?": "question", "!": "exclamation", "#": "hash",
                    "+": "heavy_plus_sign", "-": "heavy_minus_sign"
                }
                emojis.append(f":{special_char_to_emoji.get(char)}:")
            
            else:
                emojis.append(char)

        await ctx.respond("".join(emojis))

    # @slash_command(guild_ids=[918349390995914792], description="RIP")
    # async def rip(self, ctx, member: Option(discord.Member, "Mention a member", required=False, default=None)):
    #     if not member:
    #         member = ctx.author

    #     rip = Image.open("C:\\Users\\SOUMITRI\\Downloads\\rip.jpg")
    #     asset = member.avatar_url_as(size=128)
    #     data = BytesIO(await asset.read())
    #     pfp = Image.open(data)

    #     pfp = pfp.resize((185, 184))

    #     rip.paste(pfp, (100, 244))

    #     rip.save("prip.jpg")

    #     file = discord.File("prip.jpg")
    #     embed = discord.Embed(title=f"RIP {member.mention}:skull_crossbones:")
    #     embed.set_image(url="attachement://prip.jpg")
    #     embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Buried by {ctx.author.name} :skull:")
    #     await ctx.respond(file=file, embed=embed)
    #     await ctx.respond(file=discord.File("prip.jpg"))

    @slash_command(guild_ids=[918349390995914792], description="Hug another member!")
    async def hug(self, ctx, member: Option(discord.Member, "Mention a member", required=False, default=None)):
        if not member:
            member = ctx.author
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/hug") as r:
                    data = await r.json()
                    gif_url = data["link"]

                    embed = discord.Embed(description=f"Here's a hug for you **{member.display_name}**!", colour=discord.Colour.random())
                    embed.set_image(url=gif_url)
                    await ctx.respond(embed=embed)
        else:            
            author = ctx.author
            async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://some-random-api.ml/animu/hug") as r:
                        data = await r.json()
                        gif_url = data["link"]

                        embed = discord.Embed(description=f"**{author.display_name}** hugs **{member.display_name}**!", colour=discord.Colour.random())
                        embed.set_image(url=gif_url)
                        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[918349390995914792], description="Wink at another member!")
    async def wink(self, ctx, member: Option(discord.Member, "Mention a member", required=False, default=None)):
        if not member:
            member = ctx.author
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/wink") as r:
                    data = await r.json()
                    gif_url = data["link"]

                    embed = discord.Embed(description=f"**{member.display_name}** is winking", colour=discord.Colour.random())
                    embed.set_image(url=gif_url)
                    await ctx.respond(embed=embed)
        else:            
            author = ctx.author
            async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://some-random-api.ml/animu/wink") as r:
                        data = await r.json()
                        gif_url = data["link"]

                        embed = discord.Embed(description=f"**{author.display_name}** winks at **{member.display_name}**", colour=discord.Colour.random())
                        embed.set_image(url=gif_url)
                        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[918349390995914792], description="Pat another member!")
    async def pat(self, ctx, member: Option(discord.Member, "Mention a member", required=False, default=None)):
        if not member:
            member = ctx.author
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/pat") as r:
                    data = await r.json()
                    gif_url = data["link"]

                    embed = discord.Embed(description=f"Here's a pat for you **{member.display_name}**", colour=discord.Colour.random())
                    embed.set_image(url=gif_url)
                    await ctx.respond(embed=embed)
        else:            
            author = ctx.author
            async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://some-random-api.ml/animu/pat") as r:
                        data = await r.json()
                        gif_url = data["link"]

                        embed = discord.Embed(description=f"**{author.display_name}** pats **{member.display_name}**", colour=discord.Colour.random())
                        embed.set_image(url=gif_url)
                        await ctx.respond(embed=embed)

    @slash_command(guild_ids=[918349390995914792], description="Random fact")
    async def fact(self, ctx):
        api_url = f"https://api.api-ninjas.com/v1/facts?limit=1"
        response = requests.get(api_url, headers={'X-Api-Key': API_NINJAS_KEY})
        if response.status_code in range(200, 299):
            response = response.json()
            fact = response[0]["fact"]
            embed = discord.Embed(title="**Did you know?**", description=f"`{fact}`", colour=discord.Colour.random())
            await ctx.respond(embed=embed)
        
        else:
            await ctx.respond("Something went wrong. Please try again.")

    @slash_command(guild_ids=[918349390995914792], description="Watch YouTube together with friends in a voice channel!")
    async def watchtogether(self, ctx: commands.Context, channel: Option(discord.VoiceChannel, "Enter the name of the voice channel", required=False, default=None)):
        """Watch youtube together with your friends!"""
        if channel == None:
            channel = ctx.author.voice.channel
        try:
            link = await channel.create_activity_invite(discord.enums.EmbeddedActivity.watch_together, unique = False)
            await ctx.respond(f"Click the blue link!\n{link}")
        except:
            await ctx.respond("You need to be in a voice channel to play! \nOr specify a voice channel")

def setup(bot):
    bot.add_cog(Fun(bot))