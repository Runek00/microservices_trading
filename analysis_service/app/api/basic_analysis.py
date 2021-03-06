from app.api.service import get_data, send_buy
import pandas as pd


async def start_analysis():
    data = await get_data()
    stats = await calculate_stats(data)
    await send_buy(get_buy_signal(stats))


async def calculate_stats(df: pd.DataFrame):
    # df.
    return pd.DataFrame()


async def get_buy_signal(df: pd.DataFrame):
    return []
