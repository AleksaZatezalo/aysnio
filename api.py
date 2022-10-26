"""
Author: Aleksa Zatezalo
Date: October 2022
Description: A Fake API used to learn asyncio.
"""

import asyncio

async def fetch_data():
    print("Fetching Data...")
    await asyncio.sleep(2.5)
    print("Data fetched!")

    return 'API Data'