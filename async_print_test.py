import asyncio


async def print_counter(x: int):
    for number in range(x):
        print(number)
        await asyncio.sleep(.5)


async def start(x: int):
    coroutines = []

    for _ in range(x):
        coroutines.append(
            asyncio.create_task(print_counter(x))
        )

    await asyncio.wait(coroutines)


user_count = int(input('Number of functions: '))
asyncio.run(start(user_count))
