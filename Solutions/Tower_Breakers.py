
import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# def towerBreakers(n, m):
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        # result = towerBreakers(n, m)
        if m == 1:
            result = 2
        else:
            if n % 2 == 0:
                result = 2
            else:
                result = 1

        fptr.write(str(result) + '\n')

    fptr.close()
