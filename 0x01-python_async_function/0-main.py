#!/usr/bin/env python3

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))  # Uses default max_delay = 10
print(asyncio.run(wait_random(5)))  # Uses max_delay = 5
print(asyncio.run(wait_random(15))) # Uses max_delay = 15

