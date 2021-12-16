# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 18:16:43 2021

@author: vigilbushido
"""

import asyncio
from aiohttp import ClientSession

base_url = 'http://httpbin.org/'

async def count():
    for i in [1,2,3,4,5,6,7,8]:
        print("counting: ", i)
        await asyncio.sleep(1)
        
async def get_delay(seconds):
    endpoint = f'/delay/{seconds}'
    
    print(f'Getting with {seconds} delay ...')
    
    async with ClientSession() as session:
        async with session.get(base_url+endpoint) as response:
            response = await response.read()
            print("response: ", response)

async def main():
    await asyncio.gather(get_delay(5),count())
  
    
try:
    loop = asyncio.get_running_loop()
except RuntimeError:  # if cleanup: 'RuntimeError: There is no current event loop..'
    loop = None

if loop and loop.is_running():
    print('Async event loop already running')
    tsk = loop.create_task(main())
    # ^-- https://docs.python.org/3/library/asyncio-task.html#task-object)
else:
    print('Starting new event loop')
    asyncio.run(main())

print('Okay! all finished getting request.')