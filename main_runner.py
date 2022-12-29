# Please refer to README.md for details.

from datetime import datetime
import sys
import os

from abstract_metric_handler import AbstractMetricHandler, CarsRecord
from daily_cars_metric_handler import DailyCarsMetricHandler
from intervals_with_most_cars_metric_handler import IntervalsWithMostCarsMetricHandler
from time_period_with_least_cars_metric_handler import TimePeriodWithLeastCarsMetricHandler
from total_cars_metric_handler import TotalCarsMetricHandler


def _getMetricHandlers() -> list[AbstractMetricHandler]: 
    return [
        TotalCarsMetricHandler(),
        DailyCarsMetricHandler(),
        IntervalsWithMostCarsMetricHandler(),
        TimePeriodWithLeastCarsMetricHandler()
    ]


def _printOutput(filepath, metric_handlers, pretty_print):
    if pretty_print:
        print("Generating Metrics using the filepath: {0}".format(filepath))
    for handler in metric_handlers:
        if pretty_print:
            print(type(handler).__name__)
        print(handler.outputAsString())


def _parseAndValidate(input_line) -> CarsRecord:
    input_arr = input_line.split()
    if len(input_arr) < 2:
        raise Exception(
            f"Expected input line format: '2021-12-01T05:00:00 5', Found: {input_line}"
        )
    timestamp = datetime.fromisoformat(input_arr[0])
    return CarsRecord(timestamp, int(input_arr[1]))


def run(filepath, metric_handlers, pretty_print=False):
    with open(filepath) as fd:
        for input_line in fd:
            input_line = input_line.strip()
            if not input_line:
                continue
            record = _parseAndValidate(input_line)
            for handler in metric_handlers:
                handler.addRecord(record)

    _printOutput(filepath, metric_handlers, pretty_print)


def main():
    if len(sys.argv) < 2:
        raise Exception(
            "Required the input filepath, Usage: python3 main_runner.py <input_filepath>")
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        raise Exception(f"{filepath} does not exist")

    optional_args = sys.argv[2:]
    pretty_print = 'pp' in optional_args or 'pretty_print' in optional_args

    run(filepath, _getMetricHandlers(), pretty_print)


if __name__ == "__main__":
    main()
