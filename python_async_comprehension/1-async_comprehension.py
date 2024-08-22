#!/usr/bin/env python3

"""this module uses async comprehension to iterate"""
import typing
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Uses async for to iterate"""
    async for _ in range(10):
        await asyncio.sleep(1)
        return random.randrange(0, 10)
