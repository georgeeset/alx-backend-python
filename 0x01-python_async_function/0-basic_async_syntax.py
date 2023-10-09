#!/usr/bin/env python3
"""
Basic async function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function that delays at random seconds within the range of
    max_delay argument.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
