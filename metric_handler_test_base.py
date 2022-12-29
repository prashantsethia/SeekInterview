import unittest

from abstract_metric_handler import AbstractMetricHandler, CarsRecord


class TestMetricHandlerBase(unittest.TestCase):
    
    # Adds records to metric Handler and verifies the output.
    def _run_and_test(self, metric_handler: AbstractMetricHandler, records: list[CarsRecord], expected_output: list[str]) -> None:
        for record in records:
            metric_handler.addRecord(record)
        self.assertEqual(metric_handler.outputAsString(), '\n'.join(expected_output))

    # When there are no records added to metric Handler.
    def _test_empty_output(self, metric_handler: AbstractMetricHandler, expected_output='') -> None:
        self.assertEqual(metric_handler.outputAsString(), expected_output)
        

        
   

