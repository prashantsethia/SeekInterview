Refer to AIPS Coding Challenge (002).pdf for problem details.


==================
ASSUMPTIONS
==================

* Input File is sorted by time.

* Timestamps are not repeated in the file.

* All timestamps belong to same timezone.

* For metric "top 3 half hours with most cars" and "1.5 hour period with least cars", 
    we favor the time periods with most recent timestamp when there are multiple solutions.

* For metric "1.5 hour period with least cars": 
    - we only consider 3 contiguous half hours present in the sample input file.
    - it returns empty output, when there are no 3 contiguous half hours present in the file.



===================
HOW TO RUN THE CODE
===================

$ cd SeekCodingChallenge

$ python3 main_runner.py <input_filepath>

$ python3 main_runner.py <input_filepath> pretty_print

# 'pretty_print' or 'pp': Prints additional info to make it easier to read the output.


Outputs the metrics separated by newline:
- The number of cars seen in total
- Sequence of lines containing "date(yyyy-mm-dd) {number of cars seen for that day}"
- Top 3 half hours with maximum number of cars sorted by number of cars, "timestamp(yyyy-mm-ddThh:mm:ss) {number of cars for timestamp}"  
- Contiguous 3 half hours with least number of cars sorted by timestamp, "timestamp(yyyy-mm-ddThh:mm:ss) {number of cars for timestamp}"



====================
HOW TO RUN UNITTESTS
====================

$ cd SeekCodingChallenge

Run single test file: $ python -m unittest total_cars_metric_handler_test.py -v

Run all test files: $ python3 -m unittest discover -s .  -p "*_test.py" -v



====================
CODE STRUCTURE
====================

Main file: main_runner.py

Metrics are defined in the corresponding *_metric_handler.py and their unittests in *_test.py

integration_test.py for end to end tests. 

test_data contains sample input.txt and expected_output.txt.








