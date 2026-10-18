import asyncio
import time
''' Sync
def fetch_data(task):
    print(f"task {task} started")
    time.sleep(2)
    print(f"task {task} completed")
'''
#Async 

async def fetch_data(task):
    print(f'Task {task} Started')
    await asyncio.sleep(2)
    print(f'Task {task} Completed')

async def main():

 start = time.time()
 await asyncio.gather(
 fetch_data(1),
 fetch_data(2),
 fetch_data(3))
 end = time.time()
 print('Total time : ' ,round(end - start,2))


asyncio.run(main())
#print('Total time : ' ,(end - start,2))