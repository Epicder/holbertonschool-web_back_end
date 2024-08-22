#!/usr/bin/env python3

import typing
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.Generator[float, None, None]:
    async for _ in range(10):
     return random.randrange(0, 10)
