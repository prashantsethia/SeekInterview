from datetime import datetime
import unittest

from main_runner import _parseAndValidate

class MainRunnerTest(unittest.TestCase):
    
    def testInvalidInputCarsRecord(self):
        invalid_inputs = [
            '2022-01-12 40'
            '2022-01-12T00:00:00',
            '2022-01-12T1:0 10'
        ]
        for input in invalid_inputs:
            with self.assertRaises(Exception):
                _parseAndValidate(input)
    
    def testValidInputCarsRecord(self):
        cars_record = _parseAndValidate('2022-01-12T00:00:00 20')
        self.assertEqual(cars_record.num_cars, 20)
        self.assertEqual(cars_record.timestamp, datetime.fromisoformat('2022-01-12T00:00:00'))


if __name__ == '__main__':
    unittest.main()
