# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# list=[x,y,z]
# print(list)

# list=[(i,j,k) for i in range (0, x+1) for j in range (0 ,x+1) for k in range (0, x+1)]
# comp_list=[i for i in range (list)]
# print(comp_list)

# variable1 = "apple"
# variable2 = "banana"
# list=["apple","banana"]
# result_list = [] #empty list

# for var1 in (list):
#     for var2 in (list):
#         result_list.append((var1, var2))

# print(result_list)
# new_list=[[var1,var2,var3] for var1 in list for var2 in list for var3 in list if (var1 + var2+ var3)!= n]
# print(new_list)


# final code

x = int(input())
y = int(input())
z = int(input())
n = int(input())

list=[[i,j,k] for i in range (0, x+1) for j in range (0 ,y+1) for k in range (0, z+1)if (i+j+k)!=n]
print(list)

#today i lerant

# the var1 is temp variable 
# for var1 in (list) means that var1 will take first value i.e.. apple and execute the loop for that one value and then it will take second value
# see output for better understanding 
# comprehension for loop