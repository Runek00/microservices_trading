import unittest
import asyncio
from app.api.supplier import get_sample_data, supply_data
from types import GeneratorType


class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.gen = get_sample_data()
        self.data = asyncio.run(supply_data())

    def testGetSampleData(self):
        self.assertIsInstance(self.gen, GeneratorType)
        try:
            next(self.gen)
        except TypeError:
            self.fail("get_sample_data doesn't return a generator!")
        self.assertEquals(len(next(self.gen)), len(next(self.gen)))

    def testSupplyData(self):
        self.assertIsInstance(self.data, list)
