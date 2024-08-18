#!/usr/bin/env python3

"""this module returns a asyncio task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a asyncio task that waits for a random delay"""
    task = asyncio.create_task(wait_random(max_delay))
    return task

