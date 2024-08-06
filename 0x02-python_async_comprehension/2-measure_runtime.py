#!/usr/bin/env python3
'''
The Async gather 2-measure_runtime
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
     executes comprehension 4 times in parallel, returns runtime
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for n in range(4)))
    end = time.time()
    return end - start
