import asyncio
import time

# Sync Method
def greet():
    print('hello world')
    time.sleep(3)
    print('hello world 2')

async def plug():
    start = time.time()
    print('This is Secoud Function ')
    await asyncio.sleep(3)
    print('And This part After the Await')     
    end = time.time()
asyncio.run(plug())
greet()