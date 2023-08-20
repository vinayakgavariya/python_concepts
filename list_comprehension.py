# we can append multiple values in list in shorter form

#making the code compact

"""List comprehension is an elegant way to define and create lists based on existing lists.

List comprehension is generally more compact and faster than normal functions and loops for creating list."""


# syntax
# newlist = [expression for item in iterable if condition == True]
# condition is like a filter
#iterable can be any iterable object like list, tuple,set
#expression is current item in iteration

newlist = ['hello' for x in fruits]

l=[]
for a in range(1,101):
    l.append (a)
print (l)

# using list comprehension

n=[m for m in range(1,101)]
print(n)

#condition in comprehension

n=[m for m in range(1,101) if  m%2==0]
print(n)
# doubts
# why m and m are same and how it's working

#converting string into list

s="hello"
d=[g for g in s]
print(d)

# comp_list=[i for i in range (list)]
# print(comp_list)

# variable1 = "apple"
# variable2 = "banana"
list=["apple","banana"]
result_list = [] #empty list


# better understanding of for loop before understanding comprehension
for var1 in (list):
    for var2 in (list):
        result_list.append((var1, var2))

print(result_list)

#today i lerant

# the var1 is temp variable 
# for var1 in (list) means that var1 will take first value i.e.. apple and execute the loop for that one value and then it will take second value
# see output for better understanding 