import math
import os
import random
import re
import sys

def calc(c):
    # Write your code here
    r = c/(2*math.pi)
    a = r*r*math.pi
    x = round(r,2)
    y = round(a,2)
    return(x,y)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    result = calc(c)

    fptr.write(str(result) + '\n')

    fptr.close()















    