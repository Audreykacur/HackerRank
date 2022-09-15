#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.


def miniMaxSum(arr):
    # Given 5 positive integers
    # find the minimum and maximum values that can be calculated by summing exactly 4 out of the 5 integers

    sum = 0
    min = 9999999999
    max = -9000000000
    for a in arr:
        sum += a
        if a < min:
            min = a

        if a > max:
            max = a

    maxs = sum - min
    mins = sum - max
    print(mins, maxs)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
