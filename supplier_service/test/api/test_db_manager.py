import app.api.db_manager as dbm
import unittest
from unittest.mock import AsyncMock, patch
from app.api.models import PriceIn
from datetime import datetime


class TestDbManagerSave(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        dbm.database.fetch_all = AsyncMock(return_value=['t1', 't2', 't3'])

    @patch('app.api.db.database.execute_many',
           new=AsyncMock(return_value=None))
    async def testSave(self):
        dict_correct = {
            "name": "tau",
            "price": 6.28,
            "time": datetime(2013, 12, 11, 23, 22, 21)
        }
        result = await dbm.save_data([PriceIn(**dict_correct)])
        self.assertEqual(result, None)
