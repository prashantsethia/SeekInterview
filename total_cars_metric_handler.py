from abstract_metric_handler import AbstractMetricHandler, CarsRecord


class TotalCarsMetricHandler(AbstractMetricHandler):
    def __init__(self):
        self._cars_seen = 0
    
    def addRecord(self, record: CarsRecord):
        self._cars_seen += record.num_cars

    def outputAsString(self) -> str:
        return f"{self._cars_seen}"
