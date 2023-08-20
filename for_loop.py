fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    modified_fruit = fruit.upper() if fruit != "banana" else fruit # this for x in fruits can be modified
    print(modified_fruit)


# better understanding of for loop before understanding comprehension
for var1 in (list):
    for var2 in (list):
        result_list.append((var1, var2))

print(result_list)

#today i lerant

# the var1 is temp variable 
# for var1 in (list) means that var1 will take first value i.e.. apple and execute the loop for that one value and then it will take second value
# see output for better understanding 