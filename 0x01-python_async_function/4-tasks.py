#!/usr/bin/env python3
"""
Alter task 1 wait_n fnction to call task_wait_random
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """call an async function and return the esult from the function"""
    my_tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay = [await task for task in asyncio.as_completed(my_tasks)]
    return delay
