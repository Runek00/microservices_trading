from app.api.db import Cryptos, engine
from typing import List
from models import PriceIn, PriceParams
import pandas as pd
from sqlalchemy import select
from datetime import datetime, timedelta


async def save_data(crypto_data: List[PriceIn]):
    with engine.connect() as conn:
        result = conn.execute(
            Cryptos.insert(), [data.dict() for data in crypto_data]
        )
        conn.commit()
    return result


async def get_prices(params: PriceParams):
    starttime = datetime.now() - timedelta(hours=params.hours_back_start)
    endtime = datetime.now() - timedelta(hours=params.hours_back_stop)
    with engine.connect() as conn:
        stmt = Cryptos.select(Cryptos.c.time >= starttime).where(Cryptos.c.time <= endtime)
        if params.name_list is not None and len(params.name_list) > 0:
            stmt = stmt.where(Cryptos.c.symbol in params.name_list)
        result = conn.execute(stmt)
    return to_output_form(result)


# TODO
def to_output_form(result):
    out = pd.DataFrame
    return out
