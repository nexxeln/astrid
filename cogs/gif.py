import discord
import giphy_client
from giphy_client.rest import ApiException
from discord.ext import commands
from discord.commands import slash_command, Option
from settings import GIPHY_API_KEY

url = "https://api.giphy.com/v1/gifs/translate"

class Gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(guild_ids=[918349390995914792], description="GIF-fy a phrase")
    async def giffy(self, ctx, phrase: Option(str, "Enter a phrase you want to GIF-fy", required=True, default="wtf")):
        ctx.defer()
        api_key = GIPHY_API_KEY
        api_instance = giphy_client.DefaultApi()

        try:
            api_response = api_instance.gifs_translate_get(api_key, phrase)
            data = api_response.data
            embed = discord.Embed(title=phrase, colour=discord.Colour.random())
            embed.set_image(url=f"https://media.giphy.com/media/{data.id}/giphy.gif")
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name} | Powered by GIPHY")

            await ctx.respond(embed=embed)
        except ApiException as e:
            await ctx.respond("Something went wrong. Please try again.")

        
def setup(bot):
    bot.add_cog(Gif(bot))