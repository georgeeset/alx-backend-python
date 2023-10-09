#!/usr/bin/env python3
"""
A fnction that measures the total execution time for another function
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time / n"""
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_spent: float = time.perf_counter() - start
    return time_spent / n
