# M = int(input())
# set1=set()
# for i in range (M ):
#     inp=set(map(int, input().split()))
#     set1.add(inp)
# print(set1)
# Read the first integer n
n = int(input())

# Read the second line of space-separated integers and create a set
set_1 = set(map(int, input().split()))

# Read the third integer m
m = int(input())

# Read the fourth line of space-separated integers and create another set
set_2 = set(map(int, input().split()))

# Print the sets
print("Set 1:", set_1)
print("Set 2:", set_2)
