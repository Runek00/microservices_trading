import os
import httpx
from datetime import datetime, timedelta
from pandas import DataFrame
from typing import List

SUPPLIER_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/supplier/'
supplier_url = os.environ.get('SUPPLIER_SERVICE_HOST_URL') or \
    SUPPLIER_SERVICE_HOST_URL

TRADER_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/trader/'
trader_url = os.environ.get('TRADER_SERVICE_HOST_URL') or \
    TRADER_SERVICE_HOST_URL


async def get_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=24)
    r = await httpx.post(f'{supplier_url}',
                         data={
                             "start_time": start_time,
                             "end_time": end_time
                             })
    return DataFrame(r.json())


async def send_buy(signals: List[str]):
    r = await httpx.post(f'{trader_url}', data={"signals": signals})
    return True if r.status_code == 200 else False
