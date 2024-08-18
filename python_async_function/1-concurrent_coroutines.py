#!/usr/bin/env python3

"""returns a list with the n elements and their respective delay"""
import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """returns a list with the n elements and their respective delay"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    delays.sort()
    return delays
