# TASK
#       Given an integer, , perform the following conditional actions:
#       If is odd, print Weird
#       If is even and in the inclusive range of to , print Not Weird
#       If is even and in the inclusive range of to , print Weird
#       If is even and greater than , print Not Weird
# INPUT FORMAT
#   A single line containing a positive integer, .
# CONSTRAINT
#   1<=n<=100
# OUTPUT FORMAT
#   Print Weird if the number is weird; otherwise, print Not Weird .
# SAMPLE INPUT 0
#   3
# SAMPLE OUTPUT 0
#   Weird
# SAMPLE INPUT 1
#   24
# SAMPLE OUTPUT 1
#   Not Weird
# SAMPLE INPUT 0
#   3
# SAMPLE OUTPUT 0
#   Weird
# EXPLANATION 0
#   n = 3
#   n is odd and odd numbers are weird, so we print Weird .
# SAMPLE INPUT 1
#   24
# SAMPLE OUTPUT 1
#   Not Weird
# Explanation 1
#   n = 24
#   n>20 and n is even, so it isn't weird. Thus, we print Not Weird

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("enter number between 1 and 100: ").strip())
    if 1 <= n <=100:
        if n%2 != 0:
            print ('Weard')
        elif 2 <= n <= 5:
            print('Not Weird')
        elif 6 <= n <= 20:
            print('Weird')
        elif n > 20:
            print('Not Weird')
    else:
        print('entered an incorrect number')
