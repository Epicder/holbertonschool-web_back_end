#!/usr/bin/env python3

"""returns a list with the n elements and their respective delay"""
import asyncio
import typing

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """returns a list with the n elements and their respective delay"""
    delays = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    delays.sort()
    return delays
