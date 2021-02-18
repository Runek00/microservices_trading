import unittest
import app.api.db as db
from sqlalchemy import Table
from datetime import datetime
from typing import List


class TestDbInit(unittest.TestCase):

    def testElementsPresent(self):
        self.assertIsNotNone(db.engine)
        self.assertIsNotNone(db.metadata)
        self.assertIsNotNone(db.database)

    def testCryptos(self):
        self.assertIsNotNone(db.cryptos)
        self.assertIsInstance(db.cryptos, Table)
        self.assertEqual(len(db.cryptos.columns), 4)


class TestDbTableInsert(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        db.metadata.create_all(db.engine)

    async def asyncSetUp(self):
        await db.database.connect()

    async def testInsert(self):
        query = db.cryptos.insert().values(name='test', price=6.28,
                                           time=datetime.now())
        result = await db.database.execute(query=query)
        self.assertIsInstance(result, int)

    def tearDown(self):
        db.metadata.drop_all(db.engine)

    async def asyncTearDown(self):
        await db.database.disconnect()


class TestDbTableBulkInsert(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        db.metadata.create_all(db.engine)

    async def asyncSetUp(self):
        await db.database.connect()

    async def testBulkInsert(self):
        values = [{"name": 'test1', "price": 6.28, "time": datetime.now()},
                  {"name": 'test2', "price": 3.14,
                   "time": datetime(2011, 11, 11)}]
        query = db.cryptos.insert()
        result = await db.database.execute_many(query=query, values=values)
        self.assertIsNone(result)

    def tearDown(self):
        db.metadata.drop_all(db.engine)

    async def asyncTearDown(self):
        await db.database.disconnect()


class TestDbTableSelect(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        db.metadata.create_all(db.engine)

    async def asyncSetUp(self):
        await db.database.connect()
        values = [{"name": 'test1', "price": 6.28, "time": datetime.now()},
                  {"name": 'test2', "price": 3.14,
                   "time": datetime(2011, 11, 11)}]
        query = db.cryptos.insert()
        await db.database.execute_many(query=query, values=values)

    async def testSelect(self):
        query = db.cryptos.select()
        result = await db.database.fetch_all(query=query)
        self.assertIsInstance(result, List)
        self.assertEquals(len(result), 2)
        self.assertEqual(result[0]['name'], 'test1')
        self.assertEqual(result[1]['time'], datetime(2011, 11, 11))
        query = db.cryptos.select(db.cryptos.c.price == 6.28)
        result = await db.database.fetch_all(query=query)
        self.assertIsInstance(result, List)
        self.assertEquals(len(result), 1)
        self.assertEqual(result[0]['name'], 'test1')

    def tearDown(self):
        db.metadata.drop_all(db.engine)

    async def asyncTearDown(self):
        await db.database.disconnect()


class TestDbTableDelete(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        db.metadata.create_all(db.engine)

    async def asyncSetUp(self):
        await db.database.connect()
        values = [{"name": 'test1', "price": 6.28, "time": datetime.now()},
                  {"name": 'test2', "price": 3.14,
                   "time": datetime(2011, 11, 11)}]
        query = db.cryptos.insert()
        await db.database.execute_many(query=query, values=values)

    async def testDelete(self):
        query = db.cryptos.delete() \
            .where(db.cryptos.c.time == datetime(2011, 11, 11))
        result = await db.database.execute(query=query)
        self.assertIsNone(result)
        query = db.cryptos.select()
        result = await db.database.fetch_all(query=query)
        self.assertEquals(len(result), 1)

    def tearDown(self):
        db.metadata.drop_all(db.engine)

    async def asyncTearDown(self):
        await db.database.disconnect()
