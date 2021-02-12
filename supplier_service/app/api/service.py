import os
import httpx

ANALYSIS_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/analysis/'
url = os.environ.get('ANALYSIS_SERVICE_HOST_URL') or ANALYSIS_SERVICE_HOST_URL


async def send_to_analysis():
    r = await httpx.get(f'{url}start')
    return True if r.status_code == 200 else False
