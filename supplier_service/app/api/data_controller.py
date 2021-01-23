from fastapi import APIRouter, HTTPException
from models import PriceParams
from app.api import db_manager
from pandas import DataFrame

data_contr = APIRouter()


@data_contr.get('/', response_model=DataFrame)
async def get_prices(payload: PriceParams):
    prices = await db_manager.get_prices(payload)
    if not prices:
        raise HTTPException(status_code=404,
                            detail='Perhaps the archives are incomplete!')
    return prices
