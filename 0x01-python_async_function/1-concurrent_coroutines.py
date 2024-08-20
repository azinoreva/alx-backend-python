#!/usr/bin/env python3

""" 
execute multiple coroutines at the same time with async
"""

import asyncio 
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n (n, max_delay):
    """Spawn wait_random n times with the specified max_delay."""
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task  # Await each completed task
        delays.append(delay)

    return delays
