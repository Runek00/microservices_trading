from app.api.db import Cryptos, engine
from typing import List
from models import PriceIn, PriceParams
import pandas as pd


async def save_data(crypto_data: List[PriceIn]):
    with engine.connect() as conn:
        result = conn.execute(
            Cryptos.insert(), [data.dict() for data in crypto_data]
        )
        conn.commit()
    return result


# TODO
async def get_prices(params: PriceParams):
    with engine.connect() as conn:
        result = conn.execute(
            Cryptos.select()
        )
    return to_output_form(result)


# TODO
def to_output_form(result):
    out = pd.DataFrame
    return out
