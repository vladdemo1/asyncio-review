import asyncio
from random import randint
from time import perf_counter
from typing import AsyncIterable

from req_http import JSONObject, http_get


MAX_POKEMON = 898


async def get_pokemon(pokemon_id: int) -> JSONObject:
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    return await http_get(pokemon_url)


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon['name'])


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


async def main() -> None:
    time_before = perf_counter()
    names = [name async for name in next_pokemon(20)]
    print(names)
    print(f'Total time (asynchronous list comprehension): {perf_counter() - time_before}.')

    time_before = perf_counter()
    async for name in next_pokemon(20):
        print(name)
    print(f'Total time (asynchronous iterable): {perf_counter() - time_before}.')

    time_before = perf_counter()
    for _ in range(20):
        pokemon_name = await get_random_pokemon_name()
        print(pokemon_name)
    print(f'Total time (synchronous): {perf_counter() - time_before}.')

    time_before = perf_counter()
    result = await asyncio.gather(*(get_random_pokemon_name() for _ in range(20)))
    print(result)
    print(f'Total time (asynchronous): {perf_counter() - time_before}.')


asyncio.run(main())