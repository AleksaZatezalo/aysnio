"""
Author: Aleksa Zatezalo
Date: October 2023
Description: A python file created to learn pythons asyncio lib.
"""

import asyncio
from time import sleep
from unittest import result
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

# Example 2: Using Async code in a sync/async fashion
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
async def kill_time(num):
    print('Running: ', num)
    await asyncio.sleep(1)
    print('Finished', num)

async def kill_time_1000():
    list_of_tasks = []
    for i in range(1, 1000+1):
        list_of_tasks.append(kill_time(i))
    asyncio.sleep(2)
    asyncio.gather(*list_of_tasks)
    print("Done!")

# Example 4: Gathering Results
async def main():
    task = asyncio.create_task(
        api.fetch_data()
    )

#    task.cancel()
#    await asyncio.sleep(3.5)
    try:
        await asyncio.wait_for(task, timeout=2)
        if task.done():
            print(task.result())
        result = await task
        print(result)
    except asyncio.CancelledError:
        print("CANCELLED")
    except asyncio.TimeoutError:
        print("TIMEOUT")

if __name__ == '__main__':
    asyncio.run(main())