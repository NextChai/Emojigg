import emojigg
import asyncio

import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def main():
    client = emojigg.Client()
    
    packs = await client.fetch_packs()
    for pack in packs:
        emojis = await pack.emojis()
        if not emojis:
            continue
        for emoji in emojis:
            print(emoji.title)

asyncio.run(main())