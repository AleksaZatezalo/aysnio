"""
Author: Aleksa Zatezalo
Date: October 2023
Description: A python file created to learn pythons asyncio lib.
"""

import asyncio
from time import sleep

# Example One: Print Numbers 1 to 5 Using two Async Functions
async def main_func():
    task = asyncio.create_task(other_function())
    print("1")
    await asyncio.sleep(1)
    print("3")
    return_value = await task
    print(return_value)

async def other_function():
    print("2")
    await asyncio.sleep(2)
    print("4")
    return 5

asyncio.run(main_func())