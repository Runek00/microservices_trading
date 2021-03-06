import unittest
from app.api.models import PriceIn, PriceOut, PriceParams
from pydantic import ValidationError
from datetime import datetime


class TestModels(unittest.TestCase):

    def testPriceIn(self):
        dict_none = {
            "name": None,
            "price": None,
            "time": None
        }
        dict_strings = {
            "name": "test",
            "price": "test",
            "time": "test"
        }
        dict_correct = {
            "name": "tau",
            "price": 6.28,
            "time": datetime(2013, 12, 11, 23, 22, 21)
        }

        self.assertRaises(ValidationError, PriceIn, **dict_none)
        self.assertRaises(ValidationError, PriceIn, **dict_strings)
        try:
            PriceIn(**dict_correct)
        except ValidationError:
            self.fail("PriceIn raised exception when it shouldn't!")

    def testPriceOut(self):
        dict_none = {
            "id": None,
            "name": None,
            "price": None,
            "time": None
        }
        dict_in = {
            "name": "tau",
            "price": 6.28,
            "time": datetime(2013, 12, 11, 23, 22, 21)
        }
        dict_correct = {
            "id": 3,
            "name": "tau",
            "price": 6.28,
            "time": datetime(2013, 12, 11, 23, 22, 21)
        }

        self.assertRaises(ValidationError, PriceOut, **dict_none)
        self.assertRaises(ValidationError, PriceOut, **dict_in)
        try:
            PriceOut(**dict_correct)
        except ValidationError:
            self.fail("PriceIn raised exception when it shouldn't!")

    def testPriceParams(self):
        dict_none = {
            "name_list": None,
            "start_time": None,
            "stop_time": None
        }
        dict_wrong_list = {
            "name_list": [1, 2, True, ['a', 'b'], {'c': 3, 4: 'd'}],
            "start_time": datetime(2013, 12, 11, 23, 22, 21),
            "stop_time": datetime(2023, 12, 11, 23, 22, 21)
        }
        dict_wrong_time = {
            "name_list": ["test1", "test2", "test3"],
            "start_time": datetime(2013, 12, 11, 23, 22, 21),
            "stop_time": ['ddd', 3]
        }
        dict_corr_no_list = {
            "start_time": datetime(2013, 12, 11, 23, 22, 21),
            "stop_time": datetime(2023, 12, 11, 23, 22, 21)
        }
        dict_corr_full = {
            "name_list": ["test1", "test2", "test3"],
            "start_time": datetime(2013, 12, 11, 23, 22, 21),
            "stop_time": datetime(2023, 12, 11, 23, 22, 21)
        }

        self.assertRaises(ValidationError, PriceParams, **dict_none)
        self.assertRaises(ValidationError, PriceParams, **dict_wrong_list)
        self.assertRaises(ValidationError, PriceParams, **dict_wrong_time)
        try:
            PriceParams(**dict_corr_no_list)
            PriceParams(**dict_corr_full)
        except ValidationError:
            self.fail("PriceIn raised exception when it shouldn't!")
