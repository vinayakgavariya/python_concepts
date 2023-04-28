# #arrays in other languages and list in python is same
#LIST IS AMAZING ALOT OF FEATURES

# list=[5,"list", 'a', "$"]
# print(list[2])

#replacing values in list
# list[2]="x" 
# print(list[2])


# while list[3]:
#     print(list[3])



import numbers


a = ["he", "is", "a", "boy "]

# printing the list using loop
for element in a:
        a[1]="is"
        a[2]="of"
        a[3]="breathe"
        # x= print(element, end=" ")
        print(element)

#coverting list into string
result = "{} {} {} {}".format(*a) 
y= result.replace("he", "hee")
print(y)

#TWO LIST 

roll_number=[1,2,3]
names=["vinayak", "vishal"]
mil =[roll_number, names] 

#APPEND
names.append("sans")
print(names)

#INSERT
names.insert(2, "and")
print(names)

#REMOVE
names.remove("vishal")
print(names)

#POP- delete according to index
#if we don't include index then last element will be deleted
names.pop(1) 
print(names)

names.pop()
print(names)

#DEL
del names[0:]
print(names)

#EXTEND
names.extend(["himanshi","harshit"])
print(names)

#MIN MAX

print(min(roll_number))
print(max(roll_number))



