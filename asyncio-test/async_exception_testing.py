import asyncio


RETURN_EXCEPTIONS = True


async def fuck_it():
    return 42


async def foo():
    print("running foo")
    raise ValueError("Foo value error.")
    return ("Foo finished.")


async def bar():
    try:
        print("running bar")
        await asyncio.sleep(1)
        return ("Bar finished.")
    except asyncio.CancelledError:
        print("Bar Cancelled.")


async def main():
    try:
        results = await asyncio.gather(
            foo(), bar(), fuck_it(),
            return_exceptions=RETURN_EXCEPTIONS
        )
        print(results)
        failed = []
        for result in results:
            print(type(result))
            if isinstance(result, Exception):
                print("exception!!!")
                print(str(result))
            try:
                result.result()
            except Exception as e:
                failed.append(result)
        print(failed)
    except ValueError as e:
        print("Value Error raised.")


asyncio.run(main())
