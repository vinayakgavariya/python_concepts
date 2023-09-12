# M = int(input())
# set1=set()
# for i in range (M ):
#     inp=set(map(int, input().split()))
#     set1.add(inp)
# print(set1)
# Read the first integer n
m = int(input())

# Read the second line of space-separated integers and create a set
set_1 = set(map(int, input().split()))

# Read the third integer m
n = int(input())

# Read the fourth line of space-separated integers and create another set
set_2 = set(map(int, input().split()))


symmetric_diff = set_1.symmetric_difference(set_2)
asc_ord= sorted(symmetric_diff)

for element in asc_ord:
    print(element)


#today i learnt

# to take input separated by a space we will use " set_2 = set(map(int, input().split()))"
# x= int(input()) is the right syntax
# symmetric difference
# sorted is used to arrange stuff in ascending order
