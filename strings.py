# strings in python can have '' or ""

# assigning a string to variable
a="mohan"

#multiline string to a variable by using three double or single quotes

b= """hello hello hello,
       mello mello mello,
       jello jello jello."""
print(b)


# strings in python are arrays of bytes representing unicode characters
# python doesn't have character data type, a single character is simply a string with a length of 1.
# square brackets can be used to access elements of stings

a="hello world"
print(a[5]) #output will be w not whitespace

# string in for loop
for x in "banana":
    print(x)

# length of the string

a ="hello, world"
print(len(a))

# check if a certain phrase is present in a string

text="the best things in life are free"
print("free" in text) # output will be true

# using if statement 

text="the best things in life are free"
if "free" in text:
    print("free in text")


# check if not present

txt="The best part"
print("best" not in txt)

# today i learnt-

#In Python (and many other programming languages), string indexing is zero-based, which means the first character of a string is at index 0, the second character is at index 1, and so on.

#doubts-
# how we can print/access whitespace in string
# why in length white spaces are counted but can't be accessed
# what is for loop x in banana

