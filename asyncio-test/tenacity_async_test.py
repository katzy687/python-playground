import asyncio
from time import perf_counter

from tenacity import retry, wait_fixed

counter = 0

RETURN_EXCEPTIONS = False


def lol_wrapper():
    @retry(wait=wait_fixed(3))
    async def lol():
        global counter
        if counter > 5 :
            return 11
        counter += 1
        print("lol")
        raise ValueError("oops")
    return lol


async def async_lol():
    return await lol_wrapper()()


async def lol_two():
    print("lol two")
    return 22



def loop_runner():
    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([async_lol(), lol_two()])
    result = loop.run_until_complete(tasks)
    loop.close()
    return result


async def main():
    try:
        results = await asyncio.gather(
            async_lol(), lol_two(),
            return_exceptions=RETURN_EXCEPTIONS
        )
        print(results)
        failed = []
        for result in results:
            print(type(result))
            try:
                result.result()
            except Exception as e:
                failed.append(result)
        print(f"failed: {failed}")
    except ValueError as e:
        print("Value Error raised.")


asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# x = loop_runner()
# print(x)
