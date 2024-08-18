#!/usr/bin/env python3

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """returns the time that wiat_n takes to run"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    final = end - start
    return final / n
