import asyncio
import time

import tenacity
from tenacity import wait_fixed, stop_after_delay, wait_random


async def io_related(name):
    print(f'{name} started')
    await asyncio.sleep(1)
    print(f'{name} finished')
    return name


async def main():
    return await asyncio.gather(
        io_related('first'),
        io_related('second')

    )  # 1s + 1s = over 1s


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())
    loop.close()
    pass
