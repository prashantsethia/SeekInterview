from contextlib import redirect_stdout
import os
import unittest

from main_runner import _getMetricHandlers, run


class IntegrationTest(unittest.TestCase):

    def tearDown(self) -> None:
        super().tearDown()
        os.remove('test_data\output.txt')

    def testOutput(self):
        with open('test_data\output.txt', 'w') as f:
            with redirect_stdout(f):
                run('test_data\input.txt', _getMetricHandlers())

        with open('test_data\output.txt') as f_output, \
            open('test_data\expected_output.txt') as f_expected_output:
            self.assertEqual(f_output.readlines(),
                             f_expected_output.readlines())


if __name__ == '__main__':
    unittest.main()
