import discord
from discord import colour
import pypokedex
import requests
import json
from PIL import Image
from discord.ext import commands
from discord.commands import slash_command, Option
from settings import OPEN_WEATHER_MAP_KEY
from pprint import pprint
from datetime import datetime
from discord.ui import Button, View


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(guild_ids=[918349390995914792], description="Tells the weather of a loaction!")
    async def weather(self, ctx, location: Option(str, "Enter a location", required=True, default=None)):
        location = location.lower()
        if location != None:
            # get weather data
            url_celsius = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPEN_WEATHER_MAP_KEY}&units=metric"
            url_fahrenheit = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPEN_WEATHER_MAP_KEY}&units=imperial"

            data_celsius = json.loads(requests.get(url_celsius).content)
            data_fahrenheit = json.loads(requests.get(url_fahrenheit).content)

            weather = data_celsius["weather"]
            icon = weather[0]["icon"]
            url_icon = f"http://openweathermap.org/img/wn/{icon}@2x.png"


            temp_celsius = data_celsius["main"]
            humidity = str(temp_celsius["humidity"])
            t_celsius = str(temp_celsius["temp"])

            temp_fahrenheit = data_fahrenheit["main"]
            t_fahrenheit = str(temp_fahrenheit["temp"])

            location = location.title()
            embed = discord.Embed(title=f"Weather report for {location}", colour=ctx.author.colour, timestamp=datetime.utcnow())
            embed.add_field(name="Description", value=(weather[0]["description"]).title(), inline=False)
            embed.add_field(name="Temperature", value=f"{t_celsius} °C  /  {t_fahrenheit} °F", inline=False)
            embed.add_field(name="Humidity", value=f"{humidity}%")
            embed.set_thumbnail(url=url_icon)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

            await ctx.respond(embed=embed)
        else:
            await ctx.respond("Please specify a location.")

    @slash_command(guild_ids=[918349390995914792], description="Gives information about a Pokémon")
    async def pokedex(self, ctx, name: Option(str, "Enter the name of the Pokémon", required=True, default="pikachu")):
        name = name.lower()
        button = Button(label="More info", style=discord.ButtonStyle.link, url=f"https://www.pokemon.com/us/pokedex/{name}", emoji="ℹ️")
        view = View(button)
        pokemon = pypokedex.get(name=name)
        type = pokemon.types
        type = [t.title() for t in type]
        height = pokemon.height / 10.0
        weight = pokemon.weight/ 10.0

        if "Fire" in type:
            embed = discord.Embed(title=pokemon.name.title(), colour=discord.Color.red())
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)
        
        elif "Water" in type:
            embed = discord.Embed(title=pokemon.name.title(), colour=discord.Color.blue())
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)

        elif "Grass" in type:
            embed = discord.Embed(title=pokemon.name.title(), colour=discord.Color.green())
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)

        elif "Electric" in type:
            embed = discord.Embed(title=pokemon.name.title(), colour=discord.Color.gold())
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)
        
        elif "Psychic" in type:
            embed = discord.Embed(title=pokemon.name.title(), colour=discord.Color.purple())
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)
        
        elif "Rock" in type:
            embed = discord.Embed(title=pokemon.name.title(), colour=discord.Color.grey())
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)

        elif "Dark" in type:
            embed = discord.Embed(title=pokemon.name.title(), colour=discord.Color.black())
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)

        elif "Fairy" in type:
            embed = discord.Embed(title=pokemon.name.title(), colour=discord.Color.nitro_pink())
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)
        
        else:
            embed = discord.Embed(title=pokemon.name.title(), colour=ctx.author.colour)
            embed.set_thumbnail(url=pokemon.sprites.front.get("default"))
            embed.add_field(name="Pokédex Number", value=f"#{str(pokemon.dex)}", inline=False)
            embed.add_field(name="Height", value=f"{height} m", inline=True)
            embed.add_field(name="Weight", value=f"{weight} kg", inline=False)
            embed.add_field(name="Type", value=", ".join(type), inline=False)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
            await ctx.respond(embed=embed, view=view)

    @slash_command(guild_ids=[918349390995914792], description="Defines a word")
    async def dictionary(self, ctx, word: Option(str, "Enter the word", required=True, default="mask")):
        button = Button(label="More info", style=discord.ButtonStyle.link, url=f"https://www.merriam-webster.com/dictionary/{word}", emoji="ℹ️")
        view = View(button)

        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}")
        if response.status_code in range(200, 299):
            wordx = response.json()
            the_dictionary = wordx[0]
            meanings = the_dictionary["meanings"]
            definitions = meanings[0]
            definition = definitions["definitions"]
            meaningg = definition[0]
            meaning = meaningg["definition"]
            example = meaningg.get("example", ["None"])
            synonyms_list = meaningg.get("synonyms", ["None"])
            if isinstance(synonyms_list, str):
                synonyms_list = [synonyms_list]
            synonyms = ", ".join(synonyms_list)
            
            if example == ['None']:
                embed = discord.Embed(title=f"{word.title()}", colour=discord.Colour.dark_theme())
                embed.add_field(name="Definition", value=f"`{meaning}`", inline=False)
                embed.add_field(name="Synonyms", value=f"`{synonyms}`", inline=False)
            else:
                embed = discord.Embed(title=f"{word.title()}", colour=discord.Colour.dark_theme())
                embed.add_field(name="Definition", value=f"`{meaning}`", inline=False)
                embed.add_field(name="Usage", value=f"`{example}`", inline=False)
                embed.add_field(name="Synonyms", value=f"`{synonyms}`", inline=False)

            await ctx.respond(embed=embed, view=view)

        else:
            embed = discord.Embed(description="Word not found. Please try again.", colour=discord.Colour.dark_theme())
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Utilities(bot))