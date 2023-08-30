#Once a set is created, you cannot change its items, but you can add new items.
#You cannot access items in a set by referring to an index or a key.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)   # add set to set
thisset.add("orange")    # add item in set

print(thisset)

thisset1={"hello", "world"}
mylist = ["kiwi", "orange"]

thisset1.update(mylist)
print(thisset1)



# sets methods

# .add for adding values

# remove set items

set ={"a", "b"}
thisset.remove("a") # if item doesn't exist then remove will throw an error
print(set)

set1={"B", "C"}
thisset.discard("C") #discard will not give error if item doens't exist
print(set1)

# .clear empties the set

set2 ={"c", "e"}

del set2
print(set2)

set3={"a", "b"}
print(set3)
