from app.api.db import Cryptos, engine
from typing import List
from models import PriceIn, PriceParams


async def save_data(crypto_data: List[PriceIn]):
    with engine.connect() as conn:
        result = conn.execute(
            Cryptos.insert(), [data.dict() for data in crypto_data]
        )
        conn.commit()
    return result


async def get_prices(params: PriceParams):
    with engine.connect() as conn:
        stmt = Cryptos \
            .select(Cryptos.c.time >= params.start_time) \
            .where(Cryptos.c.time <= params.stop_time)
        if params.name_list is not None and len(params.name_list) > 0:
            stmt = stmt.where(Cryptos.c.symbol in params.name_list)
        result = conn.execute(stmt)
    return result
