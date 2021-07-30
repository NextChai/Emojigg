import emojigg
import asyncio

import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def main():
    client = emojigg.Client()
    
    emoji = await client.fetch_emoji_by('id', 6188)

asyncio.run(main())