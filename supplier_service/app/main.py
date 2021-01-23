from apscheduler.schedulers.blocking import BlockingScheduler
import app.api.supplier as supplier
import asyncio


sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=10)
def get_data():
    asyncio.run(supplier.get_data())


sched.start()
