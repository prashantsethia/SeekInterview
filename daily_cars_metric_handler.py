from collections import OrderedDict
from abstract_metric_handler import AbstractMetricHandler, CarsRecord


class DailyCarsMetricHandler(AbstractMetricHandler):
    def __init__(self):
        self._date_to_num_cars = OrderedDict()

    def addRecord(self, record: CarsRecord):
        date = record.timestamp.date()
        self._date_to_num_cars[date] = self._date_to_num_cars.get(
            date, 0) + record.num_cars

    def outputAsString(self) -> str:
        output = []
        for date, num_cars in self._date_to_num_cars.items():
            output.append(f"{date.isoformat()} {num_cars}")
        return '\n'.join(output)
