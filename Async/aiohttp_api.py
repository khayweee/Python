"""
Asyncio with LTA Bus stop arrival time

Sync Completed in 0.8882787227630615s
ASync Completed in 0.13811182975769043s
"""

import asyncio

import aiohttp
import time
import requests
import time
import os
from dotenv import load_dotenv

# Loading APIKEY
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
API_KEY = os.environ.get("API_KEY")

busstops = [
'01112',
'01113',
'05013',
'05022',
'07031',
'09048',
'10169',
'11169',
'17159',
'17239',
'41079',
'43419',
'44259',
'44251',
'46088',
'54261',
'59049',
'63059',
'66339',
'71079',
'71091',
'71099',
'72019',
'72069',
'75051',
'76109',
'76241',
'81111',
'82061',
'83101',
'84049',
'84059',
'85091',
'85099',
'92049',
]

""" SYNC """
time_start = time.time()
for busstop in busstops:
    url = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode={busstop}'
    headers = {'AccountKey' : API_KEY,
               'accept' : 'application/json'}
    r = requests.get(url, headers=headers)
    #print(r.status_code)

print("Sync Completed in {}".format(time.time()-time_start))

""" ASYNC """
def get_tasks(session, url, items, **kwargs):
    tasks = []
    for item in items:
        tasks.append(session.get(url.format(busstop=item), **kwargs))
    return tasks

async def get_busstops():
    url = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode={busstop}'
    headers = {'AccountKey' : API_KEY,
               'accept' : 'application/json'}
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session, url, busstops, headers=headers)
        responses = await asyncio.gather(*tasks)
        for r in responses:
            pass
            #print(r.status)

time_start = time.time()
asyncio.run(get_busstops())
print("ASync Completed in {}".format(time.time()-time_start))