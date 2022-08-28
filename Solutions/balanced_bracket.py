#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    for i in s:
        if i == "(":
            stack.append(0)
        elif i == ")":
            if len(stack)>0 and stack[-1] == 0:
                stack.pop()
            else:
                return -1
        if i == "[":
            stack.append(4)
        elif i == "]":
            if len(stack)>0 and stack[-1] == 4:
                stack.pop()
            else:
                return -1
        if i == "{":
            stack.append(2)
        elif i == "}":
            if len(stack)>0 and stack[-1] == 2:
                stack.pop()
            else:
                return -1
    if len(stack) == 0:
        return 0
    else:
        return -1
def check(s):
    # isBalanced(s)
    if isBalanced(s) == 0:
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = check(s)


        fptr.write(result + '\n')

    fptr.close()
