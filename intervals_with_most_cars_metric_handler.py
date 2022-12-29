from copy import copy
import heapq
from operator import itemgetter
from abstract_metric_handler import AbstractMetricHandler, CarsRecord


class IntervalsWithMostCarsMetricHandler(AbstractMetricHandler):
    def __init__(self, num_output_intervals=3):
        self._min_heap = []
        self._max_heap_size = num_output_intervals

    def addRecord(self, record: CarsRecord):
        # Heap item contains (num_cars, timestamp), first element is used as heap variant
        if len(self._min_heap) < self._max_heap_size:
            heapq.heappush(self._min_heap, (record.num_cars, record.timestamp))
        # new record has more cars than min till now, 
        # favoring the most recent timestamp when number of cars seen are same.
        elif self._min_heap[0][0] <= record.num_cars:
            heapq.heappushpop(
                self._min_heap, (record.num_cars, record.timestamp))

    def outputAsString(self) -> str:
        return '\n'.join(
            [f'{item[1].isoformat()} {item[0]}'
             for item in sorted(self._min_heap, key=itemgetter(0), reverse=True)]
        )
