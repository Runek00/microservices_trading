from apscheduler.schedulers.blocking import BlockingScheduler
import app.api.supplier as supplier
import asyncio
from fastapi import FastAPI
from app.api.db import metadata, database, engine


sched = BlockingScheduler()

metadata.create_all(engine)

app = FastAPI(docs_url="/api/v1/supplier/docs")


@sched.scheduled_job('interval', seconds=10)
def get_data():
    asyncio.run(supplier.supply_data())


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

sched.start()
