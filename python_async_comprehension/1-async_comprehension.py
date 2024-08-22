#!/usr/bin/env python3

"""this module uses async comprehension to iterate"""
import typing
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Uses async for to iterate"""
    value = [item async for item in async_generator()]
    return value