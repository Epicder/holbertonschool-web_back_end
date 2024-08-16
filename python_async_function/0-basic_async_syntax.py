#!/usr/bin/env python3

"""This module waits a random amount of time"""
import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """Simulate a random delay between 0 and max_delay seconds."""
    await asyncio.sleep(random.random() * max_delay)
    return random.random() * max_delay
