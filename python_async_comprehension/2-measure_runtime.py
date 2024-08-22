#!/usr/bin/env python3
"""this mdule measure the time to complete the async comp."""
import typing
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_time() -> float:
    """measures the time it takes to execute an async comprehension."""
    start_time = asyncio.get_event_loop().time()
    await async_comprehension()
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
