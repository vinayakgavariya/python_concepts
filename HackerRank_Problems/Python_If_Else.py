# Question Link:- https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#Solution:- 

#!/bin/python3

import math
import os
import random
import re
import sys



# if __name__ == '__main__':
#     n = int(input().strip())

n=int(input())
if n%2==0:
    if 2<n<5:
        print("Not Weird")
    if 6<n<=20:
        print ("Weird")
    if n>20:
        print ("Not Weird")
else:
    print("Weird")
 
# things learnt-

# 1. == is used for checking values

#one of the hidden test case failed
# inclusive 1 to 4 means 1,2,3,4
# exclusive 1 to 5 means 1,2,3,4

