import unittest
import app.api.db_manager as dbm
from unittest.mock import AsyncMock, patch, ANY
from app.api.models import PriceIn, PriceParams
from datetime import datetime


class TestDbManagerSave(unittest.IsolatedAsyncioTestCase):

    async def testSave(self):
        dict_value = {
            "name": "tau",
            "price": 6.28,
            "time": datetime(2013, 12, 11, 23, 22, 21)
        }
        with patch('app.api.db.database.execute_many',
                   new=AsyncMock(return_value=None)) as mock_em:
            result = await dbm.save_data([PriceIn(**dict_value)])
        self.assertEqual(result, None)
        mock_em.assert_called_once_with(query=ANY, values=[dict_value])

    async def testGetPrices(self):
        with patch('app.api.db.database.fetch_all',
                   new=AsyncMock(return_value=['t1', 't2', 't3'])) as mock_fa:
            dict_params = {
                "name_list": ["test1", "test2", "test3"],
                "start_time": datetime(2013, 12, 11, 23, 22, 21),
                "stop_time": datetime(2023, 12, 11, 23, 22, 21)
            }
            result = await dbm.get_prices(PriceParams(**dict_params))
            self.assertEqual(result, ['t1', 't2', 't3'])
            mock_fa.assert_called_once()
