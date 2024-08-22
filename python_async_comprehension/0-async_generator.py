#!/usr/bin/env python3
"""this module give 10 random numbers from 0 to 10"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """loop 10 times and yields a random number every time"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randrange(0, 10)
