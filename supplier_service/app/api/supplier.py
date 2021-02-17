import httpx
import random
from app.api.secret_code import secret_code
from app.api.models import PriceIn
from datetime import datetime


url = f'whatever_api/?secret_code={secret_code}'


def get_sample_data():
    ocur = ['q', 'w', 'e', 'r', 't', 'y']
    bcur = ['btc', 'usdt']
    data = []
    for o in ocur:
        for b in bcur:
            d = PriceIn(name=o+b, price=1, time=False)
            data.append(d)
    while True:
        for d in data:
            d.price += ((random.random()-0.5)/5)
            if d.name in ['qusdt', 'wusdt', 'eusdt']:
                d.price += 0.01
        yield data


data_generator = get_sample_data()


async def supply_data():
    dt = datetime.now()
    if not url.startswith('http'):
        data = next(data_generator)
    else:
        data = await httpx.get(url).json()
    data = list(filter(lambda x: x.name.endswith('usdt'), data))
    for datapoint in data:
        datapoint.time = dt
    return data
