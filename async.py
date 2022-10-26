"""
Author: Aleksa Zatezalo
Date: October 2023
Description: A python file created to learn pythons asyncio lib.
"""

import asyncio
from time import sleep
import api

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

# Example 2: Using Async code in a syncronus fashion
async def send_data(to):
    print(f'Sending data to {to}...')
    await asyncio.sleep(2)
    print(f'Data sent to {to}!')

async def sync_send():
    data = await api.fetch_data()
    print("Data: ", data)
    await send_data('Mario')

async def async_send():
    data = await api.fetch_data()
    print("Data: ", data)
    await asyncio.gather(send_data('Mario'), send_data('Luigi'))


# Example 3: Kill Time


if __name__ == '__main__':
    asyncio.run(async_send())