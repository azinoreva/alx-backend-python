#!/usr/bin/env python3
"""
Asynchronous list comprehension returns a list 
from the '0-async_generator' module.
"""
from typing import List
from importlib import import_module as using
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async_generator function. Returns list of floats 
    """
    return [i async for i in async_generator()]
