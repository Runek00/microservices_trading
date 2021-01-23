from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, Float, DateTime)
from databases import Database
import os

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

Cryptos = Table(
    'cryptos',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('symbol', String(10)),
    Column('b_price', Float),
    Column('time', DateTime)
)

database = Database(DATABASE_URI)
