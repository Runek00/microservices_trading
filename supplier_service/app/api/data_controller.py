from fastapi import APIRouter, HTTPException
from models import PriceParams
from app.api import db_manager
from app.api.db import cryptos
from typing import List, Dict

data_contr = APIRouter()


@data_contr.post('/', response_model=List[Dict])
async def get_prices(payload: PriceParams):
    prices_raw = await db_manager.get_prices(payload)
    prices = await to_dto(prices_raw)
    if not prices:
        raise HTTPException(
            status_code=404,
            detail='Perhaps the archives are incomplete!'
        )
    return prices


async def to_dto(result: List[cryptos]):
    variables = result[0].keys()
    dto = [
            {j: getattr(i, j) for j in variables}
            for i in result
        ]
    return dto
