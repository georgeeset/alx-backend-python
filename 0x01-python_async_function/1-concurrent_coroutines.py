#!/usr/bin/env python3
"""
A function that calls an async function
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """call an async function and return the esult from the function"""
    my_tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay = [await task for task in asyncio.as_completed(my_tasks)]
    return delay
