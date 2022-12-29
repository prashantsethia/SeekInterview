from datetime import datetime
import unittest

from abstract_metric_handler import CarsRecord
from intervals_with_most_cars_metric_handler import IntervalsWithMostCarsMetricHandler
from metric_handler_test_base import TestMetricHandlerBase

METRIC_HANDLER_CLASS = IntervalsWithMostCarsMetricHandler

class TestIntervalsWithMostCarsMetricHandler(TestMetricHandlerBase):

    def test_output_before_adding_records(self):
        self._test_empty_output(METRIC_HANDLER_CLASS(), expected_output='')

    # Simple case where all records have distinct no of cars seen.
    def test_simple_case(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 20),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-01-12T02:00:00'), 30),
            CarsRecord(datetime.fromisoformat('2022-01-12T03:00:00'), 40)
        ]
        expected_output = ['2022-01-12T03:00:00 40',
                           '2022-01-12T02:00:00 30',
                           '2022-01-12T00:00:00 20']
        self._run_and_test(METRIC_HANDLER_CLASS(), records, expected_output)

    # When there are two records with same number of seen cars, we return
    # most recent timestamp.
    def test_multiple_records_having_same_no_of_cars_returns_most_recent_ts(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:00:00'), 20),
            CarsRecord(datetime.fromisoformat('2022-01-12T02:00:00'), 30),
            CarsRecord(datetime.fromisoformat('2022-01-12T03:00:00'), 10)
        ]
        expected_output = ['2022-01-12T02:00:00 30',
                           '2022-01-12T01:00:00 20',
                           '2022-01-12T03:00:00 10']
        self._run_and_test(METRIC_HANDLER_CLASS(), records, expected_output)


    # When number of records seen is less than required top output intervals.
    def test_when_no_of_input_records_is_less_than_output_intervals(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:00:00'), 20),
        ]
        expected_output = ['2022-01-12T01:00:00 20', '2022-01-12T00:00:00 10']
        self._run_and_test(METRIC_HANDLER_CLASS(num_output_intervals=4), records, expected_output)


if __name__ == '__main__':
    unittest.main()
