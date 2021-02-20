from app.api.db import cryptos, database
from typing import List
from app.api.models import PriceIn, PriceParams


async def save_data(crypto_data: List[PriceIn]):
    query = cryptos.insert()
    await database.execute_many(
        query=query, values=[data.dict() for data in crypto_data])


async def get_prices(params: PriceParams):
    query = cryptos.select(cryptos.c.time >= params.start_time) \
        .where(cryptos.c.time <= params.stop_time)
    if params.name_list is not None and len(params.name_list) > 0:
        query = query.where(cryptos.c.name in params.name_list)
    result = await database.fetch_all(query=query)
    return result
