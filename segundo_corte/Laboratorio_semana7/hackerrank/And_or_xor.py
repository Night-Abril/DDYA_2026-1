#Trabajado en Hacker Rank: https://www.hackerrank.com/challenges/and-xor-or/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andXorOr' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def andXorOr(a):
    
    stack = []
    max_value = 0

    for num in a:

        while stack:

            max_value = max(max_value, num ^ stack[-1])

            if stack[-1] > num:
                stack.pop()
            else:
                break

        stack.append(num)

    return max_value
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()