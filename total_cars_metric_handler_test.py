from datetime import datetime
import unittest

from abstract_metric_handler import CarsRecord
from metric_handler_test_base import TestMetricHandlerBase
from total_cars_metric_handler import TotalCarsMetricHandler


METRIC_HANDLER_CLASS = TotalCarsMetricHandler


class TestTotalCarsMetricHandler(TestMetricHandlerBase):

    def test_output_before_adding_records(self):
        self._test_empty_output(METRIC_HANDLER_CLASS(), expected_output='0')

    def test_output(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:00:00'), 20),
            CarsRecord(datetime.fromisoformat('2022-01-12T02:00:00'), 10)
        ]
        self._run_and_test(METRIC_HANDLER_CLASS(), records, expected_output=['40'] )


if __name__ == '__main__':
    unittest.main()
