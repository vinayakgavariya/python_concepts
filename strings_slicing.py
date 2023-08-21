name ="Mango"
print(name[0:6])
len1=len(name)
print("name is a", len1,"letter word")

#string is sequence of character

#we use [] for slicing
print(name[0:4]) # including 0 but 4th will not be included
print(name[1:4]) #including 1 but 4th will not included
print(name[:5]) # will include 0
print(name[0:]) #will include len

# negative indexing
print(name[0:-3]) 
print(name[0:len(name)-3]) # here -3 means len-3 so [0:2] hence ma will be printed as 2 is not counted
print(name[-1:len(name)-3])
print(name[-3:-1]) # it means [2:4]

# quiz 

nm="Harry"
print(nm[-4:-2])

