# TASK
#
#   Read two integers from STDIN and print three lines where:
#       1.The first line contains the sum of the two numbers.
#       2.The second line contains the difference of the two numbers (first - second).
#       3.The third line contains the product of the two numbers.

# INPUT FORMAT
#
#   The first line contains the first integer, a. The second line contains the second integer, .
#

# CONSTRAINTS
#   1<=a<=10^10
#   1<=b<=10^10
#

# OUTPUT FORMAT
#
# Print the three lines as explained above.
#

# SAMPLE INPUT 0
#
#   3
#   2

# SAMPLE OUTPUT 0
#
#   5
#   1
#   6

# EPLANATION 0
#   3+2 ==> 5
#   3-2 ==> 1
#   3*2 ==> 6

if __name__ == '__main__':
    a = int(input())
    b = int(input())
