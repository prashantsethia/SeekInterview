from datetime import datetime


class CarsRecord:
    def __init__(self, timestamp: datetime, num_cars: int):
        self.timestamp = timestamp
        self.num_cars = num_cars


class AbstractMetricHandler:
    def addRecord(self, record: CarsRecord):
        raise NotImplementedError

    def outputAsString(self) -> str:
        raise NotImplementedError
