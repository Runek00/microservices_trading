from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class PriceIn(BaseModel):
    name: str
    price: float
    time: datetime


class PriceOut(PriceIn):
    id: int


class PriceParams(BaseModel):
    name_list: Optional[List[str]]
    start_time: datetime
    stop_time: datetime
