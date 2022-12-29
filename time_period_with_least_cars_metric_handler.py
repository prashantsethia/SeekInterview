from collections import OrderedDict, deque
from copy import copy
from datetime import datetime, timedelta
from abstract_metric_handler import AbstractMetricHandler, CarsRecord


class TimePeriodWithLeastCarsMetricHandler(AbstractMetricHandler):
    def __init__(
        self,
        input_time_interval=timedelta(minutes=30),
        output_time_interval=timedelta(hours=1, minutes=30)
    ):
        if (input_time_interval > output_time_interval
            or input_time_interval == timedelta(0)
                or output_time_interval % input_time_interval != timedelta(0)):
            raise ValueError('Invalid time intervals')

        self._queue = deque([])
        self._max_queue_size = output_time_interval // input_time_interval
        self._input_time_interval = input_time_interval
        self._least_cars_records = []
        self._least_num_cars = None

    def addRecord(self, record: CarsRecord):
        if not self._queue:
            self._queue.append(record)
            return
        last_record = self._queue[-1]
        difference = record.timestamp - last_record.timestamp
        if difference != self._input_time_interval:
            self._queue.clear()
        elif len(self._queue) == self._max_queue_size:
            self._queue.popleft()
        self._queue.append(record)

        num_cars = sum(item.num_cars for item in self._queue)
        if (len(self._queue) == self._max_queue_size
                and (self._least_num_cars is None or num_cars <= self._least_num_cars)):
            self._least_cars_records = copy(self._queue)
            self._least_num_cars = num_cars

    def outputAsString(self) -> str:
        return '\n'.join(
            [f"{record.timestamp.isoformat()} {record.num_cars}"
             for record in self._least_cars_records]
        )
