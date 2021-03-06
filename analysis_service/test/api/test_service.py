import unittest
import app.api.service as service
from unittest.mock import Mock, AsyncMock, patch
import httpx


class TestService(unittest.IsolatedAsyncioTestCase):

    async def testGetData(self):
        respMock = Mock(spec=httpx.Response)
        respMock.status_code = 200
        respMock.json = lambda: [
            {"tc1": 1, "tc2": "one"},
            {"tc1": 2, "tc2": "two"}
        ]
        with patch('httpx._api.request',
                   new=AsyncMock(return_value=respMock)) as test_post:
            df = await service.get_data()
            self.assertIsNotNone(df)
            test_post.assert_called_once()

    async def testSendBuy(self):
        respMock = Mock(spec=httpx.Response)
        respMock.status_code = 200
        with patch('httpx._api.request',
                   new=AsyncMock(return_value=respMock)) as test_post:
            self.assertRaises(TypeError, service.send_buy)
            df = await service.send_buy(['a', 'b', 'c'])
            self.assertEqual(df, True)
            test_post.assert_called_once()
