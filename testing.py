import emojigg
import asyncio

import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def main():
    client = emojigg.Client()
    
    emojis = await client.fetch_emojis()
    logging.info(f"Total emojis: {len(emojis)}")
    
    categories = await client.fetch_categories()
    logging.info(f"Total categories: {len(categories)}")
    
    packs = await client.fetch_packs()
    logging.info(f"Total packs: {len(packs)}")
    
    await client.fetch_statistics()
    logging.info("Got stats correctly.")
    
    pack = await client.get_pack_from('name', 'lgbtq', packs=packs)
    logging.info("Found pack: {0.name}".format(pack))

asyncio.run(main())