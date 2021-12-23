import discord
from discord import emoji
from discord.ext import commands
from discord.commands import slash_command, Option

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


def setup(bot):
    bot.add_cog(Fun(bot))