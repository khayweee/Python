import asyncio


async def fetch_data():
    print('start fetching')

    """ simulate backend server call """
    await asyncio.sleep(2)
    print('done fetching')
    """ done with backend server call """
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    task2 = asyncio.create_task(print_numbers())
    task1 = asyncio.create_task(fetch_data())
    await task2
    await task1
    

asyncio.run(main())