from datetime import datetime, timedelta
import unittest

from abstract_metric_handler import CarsRecord
from intervals_with_most_cars_metric_handler import IntervalsWithMostCarsMetricHandler
from metric_handler_test_base import TestMetricHandlerBase
from time_period_with_least_cars_metric_handler import TimePeriodWithLeastCarsMetricHandler


METRIC_HANDLER_CLASS = TimePeriodWithLeastCarsMetricHandler


class TestTimePeriodWithLeastCarsMetricHandle(TestMetricHandlerBase):

    def test_output_before_adding_records(self):
        self._test_empty_output(METRIC_HANDLER_CLASS(), expected_output='')

    def test_invalid_input_output_params(self):
        with self.assertRaises(ValueError):
            # input interval is 0
            TimePeriodWithLeastCarsMetricHandler(
                input_time_interval=timedelta(0))

        with self.assertRaises(ValueError):
            # output interval is not a multiple of input interval
            TimePeriodWithLeastCarsMetricHandler(
                input_time_interval=timedelta(30), output_time_interval=timedelta(45))

        with self.assertRaises(ValueError):
            # input interval is more than output interval
            TimePeriodWithLeastCarsMetricHandler(
                input_time_interval=timedelta(30), output_time_interval=timedelta(10))

    def test_simple_case(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 5),
            CarsRecord(datetime.fromisoformat('2022-01-12T00:30:00'), 4),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:00:00'), 2),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:30:00'), 2),
            CarsRecord(datetime.fromisoformat('2022-01-12T02:00:00'), 20),
            CarsRecord(datetime.fromisoformat('2022-01-12T02:30:00'), 4),
        ]
        self._run_and_test(
            METRIC_HANDLER_CLASS(),
            records,
            expected_output=['2022-01-12T00:30:00 4',
                             '2022-01-12T01:00:00 2', '2022-01-12T01:30:00 2']
        )

    # Without the existence of 3 contiguous intervals, returns empty output.
    def test_no_contiguous_candidate_interval_exists(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-01-12T01:00:00'), 20),
            CarsRecord(datetime.fromisoformat('2022-01-12T03:00:00'), 30),
            CarsRecord(datetime.fromisoformat('2022-01-12T04:00:00'), 10)
        ]
        self._run_and_test(
            METRIC_HANDLER_CLASS(
                input_time_interval=timedelta(minutes=30),
                output_time_interval=timedelta(minutes=90)
            ),
            records,
            expected_output=[]
        )

    # Number of input records less than 3.
    def test_when_input_records_interval_is_less_than_output_interval_duration(self):
        records = [
            CarsRecord(datetime.fromisoformat('2022-01-12T00:00:00'), 10),
            CarsRecord(datetime.fromisoformat('2022-01-12T00:30:00'), 20),
        ]
        self._run_and_test(
            METRIC_HANDLER_CLASS(
                input_time_interval=timedelta(minutes=30),
                output_time_interval=timedelta(minutes=90)
            ),
            records,
            expected_output=[]
        )


if __name__ == '__main__':
    unittest.main()
