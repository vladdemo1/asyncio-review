"""
Review work asyncio
"""

import asyncio


async def start():
    print('tim')
    task = asyncio.create_task(foo('work foo func'))
    # await task
    await asyncio.sleep(.5)
    print('finished')


async def foo(text: str):
    print(text)
    await asyncio.sleep(10)


# asyncio.run(start())


async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(.5)


async def main():
    """
    First, printing start fetching
    and then print 0 1 2 3
    after this we can see print 'done fetching and dict, bcs sleep .5 (x4 times) and sleep(2) work inside fetch data'
    """

    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2


asyncio.run(main())
