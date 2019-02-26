# Robert Allen, William Blackwell, Bradley Sutton
# Implements recursive and dynamic programming versions of Fibonacci algorithm

import os
import timeit
import math
from decimal import Decimal  # used for scientific notation

# Values to be tested
FIB_NUMS = [19, 20, 30, 35, 40, 45, 50, 55]

# FILENAME and HEADER used during csv generation
FILENAME = "Fibonacci_Time.csv"
HEADERS = ["n", "F(n)", "T1: Recursive Algorithm (ms)", "T2: DP Algorithm (ms)", "(2^n)/n", "T1/T2"]

DYNAMIC_PROG_MAP = {0: 1, 1: 1}  # initialize a dict to map calculated results for DP Fib calculations


def main():
    output_to_csv(FILENAME, HEADERS, run_tests())
    print("Done.\nFile saved to " + os.getcwd() + "\\" + FILENAME)
    console_interface()


########################################################################################################################
#  Classes
########################################################################################################################
class TestResults(object):
    """
        Contains the information about each alg's test run for file output
        :param fib_num: Calculated Fibonacci number
        :type: ints
        :param time_rec: Time elapsed during recursive algorithm test
        :type: float
        :param time_dp: Time elapsed during dp algorithm test
        :type: float
        :param n: number who's Fibonacci value is being calculated
        :type: int
        """
    def __init__(self, fib_num, time_rec, time_dp, n):
        self.fib_num = fib_num
        self.time_rec = time_rec
        self.time_dp = time_dp
        self.n = n
        self.val1 = math.pow(2, n) / 2  # value of 2^n/n
        self.val2 = '%0.E' % Decimal(self.time_rec / self.time_dp)  # t1/t2 rounded used sci-notation

    # help for csv output
    def to_string(self):
        return str(self.n), str(self.fib_num), str(self.time_rec), str(self.time_dp), str(self.val1), str(self.val2)


########################################################################################################################
#  Fibonacci
########################################################################################################################
# Calculates Fibonacci Number using Recursion
def recur_fib(num):
    if num <= 1:
        return 1
    return recur_fib(num - 1) + recur_fib(num - 2)


# Calculates Fibonacci Number using Dynamic Programming
# Results of calculations saved to the DYNAMIC_PROG_MAP dictionary
def dp_fib(num):
    for i in range(2, num + 1):
        DYNAMIC_PROG_MAP[i] = DYNAMIC_PROG_MAP[i - 1] + DYNAMIC_PROG_MAP[i - 2]
    return DYNAMIC_PROG_MAP[num]


########################################################################################################################
#  Time Execution Test
########################################################################################################################
# Measures execution time of each merge sort and saves results to an array of MergeSortResult objects
# Returns the Fib value and time as a tuple
def calc_time(alg, num):
    start_time = timeit.default_timer()  # start time measure
    fib_num = alg(num)
    stop_time = timeit.default_timer()  # end time measure
    return fib_num, (stop_time - start_time) * 1000


# Loops over the FIB_NUM array and calculates the Fibonacci number of each using Recursion and DP
# The time of each method is measured and the results are stored in an array of TestResults for csv output
def run_tests():
    results = []
    for i in FIB_NUMS:
        recur_results = calc_time(recur_fib, i),  # recursion time
        dp_results = calc_time(dp_fib, i),  # dp time

        # Extract values from tuples
        fib = dp_results[0][0]
        t1 = recur_results[0][1]
        t2 = dp_results[0][1]

        # Append to results array as a new TestResults object
        results.append(TestResults(fib, t1, t2, i))
    return results


########################################################################################################################
#  Output Results
########################################################################################################################
# outputs results to csv file
def output_to_csv(filename, headers, data):
    with open(filename, 'w') as file:
        for header in headers:
            file.write(header)
            file.write(",")
        file.write("\n")
        for d in data:
            file.write(",".join(d.to_string()))
            file.write("\n")


# interface for user to request sorted and unsorted arrays of the test runs
def console_interface():
    while True:
        # Ask for algorithm to use
        print("\nSelect Recursive(R) or Dynamic(D) Fibonacci Algorithm or q to quit\n")
        user_in = input("->  ")
        try:
            if user_in == 'q':
                print("Exiting ... \n")
                break
            # Ask for value to find
            elif user_in == 'R':
                print("\nEnter a Number\n")
                user_in = input("->  ")
                print(recur_fib(int(user_in)))
            elif user_in == 'D':
                print("\nEnter a Number\n")
                user_in = input("->  ")
                print(dp_fib(int(user_in)))
        except:
            print("Invalid input: ", user_in, "\n")


########################################################################################################################
#  Run Script
########################################################################################################################
if __name__ == "__main__":
    main()
