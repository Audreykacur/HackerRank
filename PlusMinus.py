#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

# given an array of integers
# find the ratio of the arrays integers that are positive negative and zero
# print the decimal value of each fraction on a new line w 6 places after the decimal


def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for a in arr:
        if a == 0:
            zer += 1
        elif a < 0:
            neg += 1
        elif a > 0:
            pos += 1
        else:
            print("error")
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))

    # Write your code here


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
