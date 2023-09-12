# from itertools import combinations


# input_string, B = input().split()
# B =int(B)

# input_str = input_string.upper()

# combs=list(combinations(input_str, B))

# for item in combs:
#     print(''.join(item))

from itertools import combinations

# Read input as a string and an integer
input_str, B = input().split()
input_str = input_str.upper()
B = int(B)

# Convert the input string to uppercase
input_str = input_str.upper()

# Generate combinations
combs = list(combinations(input_str, B))
print(combs)
# Print the combinations
# for comb in combs:
#     print(''.join(comb))


