from collections import OrderedDict
from datetime import datetime
import unittest

from abstract_metric_handler import CarsRecord
from daily_cars_metric_handler import DailyCarsMetricHandler
from metric_handler_test_base import TestMetricHandlerBase


METRIC_HANDLER_CLASS = DailyCarsMetricHandler


class TestDailyCarsMetricHandler(TestMetricHandlerBase):

    def test_output_before_adding_records(self):
        self._test_empty_output(METRIC_HANDLER_CLASS(), expected_output='')
    
    def test_output_single_day(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:00:00'), 20),
            CarsRecord(datetime.fromisoformat('2022-01-12T02:00:00'), 10)
        ]
        self._run_and_test(METRIC_HANDLER_CLASS(), records,
                          expected_output=['2022-01-12 40'])

    def test_output_multiple_days(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:00:00'), 20),
            CarsRecord(datetime.fromisoformat('2022-02-12T02:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-02-12T14:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-02-13T02:00:00'), 10)
        ]
        self._run_and_test(METRIC_HANDLER_CLASS(), records, expected_output=[
            '2022-01-12 30',
            '2022-02-12 20',
            '2022-02-13 10'
        ])


if __name__ == '__main__':
    unittest.main()
