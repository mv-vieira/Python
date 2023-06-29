import asyncio


async def flash_correr():
    print("Flash começou a correr!")

    await asyncio.sleep(3)
    print("Flash chegou!!")

async def superman_correr():
    print("Superman começou a correr!")

    await asyncio.sleep(5)
    print("Superman chegou!!")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(flash_correr(),superman_correr()))

