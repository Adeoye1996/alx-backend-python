#!/usr/bin/env python3
""" The basics of asynchronous """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Define an asynchronous coroutine named random_wait that accepts
    an integer parameter (max_delay, defaulting to 10).
    This coroutine pauses for a random duration between 0
    and max_delay seconds (inclusive, as a float)
    before returning the duration.
    Utilizes the random module.
    """
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return ran
