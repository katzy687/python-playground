""" https://stackoverflow.com/a/53420574 """
import asyncio
from timeit import default_timer
from tenacity import retry, retry_if_result, stop_after_attempt, wait_fixed, AsyncRetrying, RetryError

ATTEMPTS = 2
DELAY_TIME = 1


async def poll_sandbox_api(sandbox_id):
    my_counter = 0
    while my_counter < ATTEMPTS:
        print(f"{sandbox_id} - attempt {my_counter+1}")
        my_counter += 1
        if my_counter < ATTEMPTS:
            await asyncio.sleep(DELAY_TIME)
    return sandbox_id

counter = 0


async def retry_poll_sandbox_api(sandbox_id):
    async for attempt in AsyncRetrying(wait=wait_fixed(DELAY_TIME)):
        with attempt:
            print(f"{sandbox_id} - attempt: {attempt.retry_state.attempt_number}")
            if attempt.retry_state.attempt_number < ATTEMPTS:
                raise Exception("fail!")
    return sandbox_id


async def while_poll_sandboxes(sandbox_list):
    sandbox_ids = await asyncio.gather(*[poll_sandbox_api(sb_id) for sb_id in sandbox_list])
    return sandbox_ids


async def retry_poll_sandboxes(sandbox_list):
    sandbox_ids = await asyncio.gather(*[retry_poll_sandbox_api(sb_id) for sb_id in sandbox_list])
    return sandbox_ids


def poll_sandboxes(sandbox_list):
    return asyncio.run(retry_poll_sandboxes(sandbox_list))


def poll_sandbox(sb_id):
    return poll_sandboxes([sb_id])[0]

print(poll_sandboxes(["abc", "def"]))
print(poll_sandbox("asdf"))

SANDBOX_ID_LIST = ["ABC", "DEF"]

print("=== while loop test ===")
start = default_timer()
res = asyncio.run(while_poll_sandboxes(SANDBOX_ID_LIST))
print(f"ran in {default_timer() - start} seconds")
print(res)

print("=== async io test ===")
start = default_timer()
res = asyncio.run(retry_poll_sandboxes(SANDBOX_ID_LIST))
print(f"ran in {default_timer() - start} seconds")
print(res)
