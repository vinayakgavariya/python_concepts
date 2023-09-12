# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A= list(map(int, input().split()))
B= list(map(int, input().split()))

result= (product(A,B))

for item in result:
    print(item, end=' ')    # this will give output separated by space in same line
