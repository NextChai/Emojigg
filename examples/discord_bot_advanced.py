from emojigg import emoji
import discord
from discord.ext import commands

import aiohttp
import emojigg


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            description='A super helpful test bot.'
        )
        self.session = aiohttp.ClientSession()
        self.emoji_gg = emojigg.Client(self.session)
        

bot = Bot() 

# Usually we do commands inside of a cog, 
# but for this example we can keep it in one file.

@commands.command(
    name='count',
    brief='Get some emojis!',
    description='Use the EmojiGG Api to get some emojis and the count of emojis.'
)
async def count(ctx):
    emojis = await bot.emoji_gg.fetch_emojis()
    
    embed = discord.Embed()
    embed.add_field(
        name='Total Emojis Found:', 
        value=len(emojis)
    )
    
    emoji = emojis[0]
    embed.add_field(
        name='First emoji:', 
        value=f'Title: {emoji.title}\n' \
            f'ID: {emoji.id}'
    )
    embed.set_image(url=emoji.image)
    
    return await ctx.send(embed=embed)

bot.run("TOKEN")