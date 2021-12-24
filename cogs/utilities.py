import discord
from discord.types.embed import EmbedAuthor
import pypokedex
import requests
import wikipedia
import json
from PIL import Image
from discord.ext import commands
from discord.commands import slash_command, Option
from settings import OPEN_WEATHER_MAP_KEY, API_NINJAS_KEY
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
        await ctx.interaction.response.defer()
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

            await ctx.interaction.followup.send(embed=embed, view=view)

        else:
            embed = discord.Embed(description="Word not found. Please try again.", colour=discord.Colour.dark_theme())
            await ctx.respond(embed=embed)

    @slash_command(guild_ids=[918349390995914792], description="Shows the air quality of a place")
    async def aqi(self, ctx, city: Option(str, "Enter the name of the city", required=True, default="new york")):
        await ctx.interaction.response.defer()
        api_url = f"https://api.api-ninjas.com/v1/airquality?city={city}"
        response = requests.get(api_url, headers={"X-Api-Key": API_NINJAS_KEY})
        button = Button(label="Learn more about AQI", style=discord.ButtonStyle.link, url=f"https://www.airnow.gov/aqi/aqi-basics/", emoji="ℹ️")
        view = View(button)
        city = city.title()
        if response.status_code in range(200, 299):
            response = response.json()
            aqi = response["overall_aqi"]
            if (aqi > 0) and (aqi<=50):
                embed = discord.Embed(title=f"Air Quality in {city}", description="Level of concern: **Good**", colour=0x56f00e)
                embed.add_field(name="AQI", value=str(aqi), inline=False)
                embed.add_field(name="Description", value="Air quality is satisfactory, and air pollution poses little or no risk.")
                await ctx.interaction.followup.send(embed=embed, view=view)

            elif (aqi > 50) and (aqi <= 100):
                embed = discord.Embed(title=f"Air Quality in {city}", description="Level of concern: **Moderate**", colour=0xf7e307)
                embed.add_field(name="AQI", value=str(aqi), inline=False)
                embed.add_field(name="Description", value="Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.")
                await ctx.interaction.followup.send(embed=embed, view=view)

            elif (aqi > 100) and (aqi <= 150):
                embed = discord.Embed(title=f"Air Quality in {city}", description="Level of concern: **Unhealthy for Sensitive Groups**", colour=0xf2670a)
                embed.add_field(name="AQI", value=str(aqi), inline=False)
                embed.add_field(name="Description", value="Members of sensitive groups may experience health effects. The general public is less likely to be affected.")
                await ctx.interaction.followup.send(embed=embed, view=view)

            elif (aqi > 150) and (aqi <= 200):
                embed = discord.Embed(title=f"Air Quality in {city}", description="Level of concern: **Unhealthy**", colour=0xcf0606)
                embed.add_field(name="AQI", value=str(aqi), inline=False)
                embed.add_field(name="Description", value="Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.")
                await ctx.interaction.followup.send(embed=embed, view=view)
            
            elif (aqi > 200) and (aqi <= 300):
                embed = discord.Embed(title=f"Air Quality in {city}", description="Level of concern: **Very Unhealthy**", colour=0x8e05e3)
                embed.add_field(name="AQI", value=str(aqi), inline=False)
                embed.add_field(name="Description", value="Health alert: The risk of health effects is increased for everyone.")
                await ctx.interaction.followup.send(embed=embed, view=view)

            elif (aqi > 300):
                embed = discord.Embed(title=f"Air Quality in {city}", description="Level of concern: **Hazardous**", colour=0x800000)
                embed.add_field(name="AQI", value=str(aqi), inline=False)
                embed.add_field(name="Description", value="Health warning of emergency conditions: everyone is more likely to be affected.")
                await ctx.interaction.followup.send(embed=embed, view=view)

        else:
            await ctx.respond("Something went wrong.")
        
    @slash_command(guild_ids=[918349390995914792], description="Get information about anything")
    async def wiki(self, ctx, topic: Option(str, "Please be as specific as possible!", required=True, default="new york")):
        await ctx.interaction.response.defer()
        topic = topic.title()
        try:
            summary = wikipedia.summary(topic, sentences=3, auto_suggest=False)
            page = wikipedia.page(topic, auto_suggest=False)

            button = Button(label="More info", style=discord.ButtonStyle.link, url=page.url, emoji="ℹ️")
            view = View(button)
            
            embed = discord.Embed(title=page.title, colour=ctx.author.colour)
            embed.add_field(name="Summary", value=f"```{summary}```")
            embed.set_thumbnail(url=page.images[0])
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name} | Powered by Wikipedia")
            await ctx.interaction.followup.send(embed=embed, view=view)

        except wikipedia.exceptions.DisambiguationError as e:
            await ctx.interaction.followup.send("Please be as specific as possible!")
        
        except wikipedia.exceptions.PageError as e:
            await ctx.interaction.followup.send(f"{topic} does not match any pages. Try another query!")

            


def setup(bot):
    bot.add_cog(Utilities(bot))