# n = int(input())
# arr = map(int, input().split()) # it was give

# this was my initial approach which was correct but the hackerrank don't support inputs in loops as it supports STDIN 

# my_list =[]
# for i in range (n):
#     my_list.append(input())
# print(list)
# print(list.sort())
# # Sample list of elements
# my_list = [5, 2, 8, 1, 3]

# Sort the list in increasing order
# sorted_list = sorted(my_list,reverse=True)

# print(sorted_list[1])  # Output: [1, 2, 3, 5, 8]

#here is the working code

n = int(input())
arr = map(int, input().split())  # map(int, input().split()): The map() function applies the int function to each element of the list obtained from input().split(). This effectively converts each space-separated input value into an integer.
#So, if the user inputs something like "1 2 3 4", the map(int, input().split()) line will convert it into an iterable of integers: map object with [1, 2, 3, 4].

print (sorted(list(set(arr)))[-2])

#today i learnt

#if the list will already sorted then it will return none

