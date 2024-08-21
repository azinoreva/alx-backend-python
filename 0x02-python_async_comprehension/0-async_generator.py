#!/usr/bin/env python3
"""
asynchronous generator function that yield 10 iterations.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Function that yields  a one second delay for 10 iterations.
    Returns: Asynchronous generator object       
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
